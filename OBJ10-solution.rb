require 'openssl'

KEY_LENGTH = 8 # TODO DES is 8 bytes

def generate_key(seed)
  key = ""
  1.upto(KEY_LENGTH) do
    key += (((seed = (214013 * seed + 2531011) & 0x7fff_ffff) >> 16) & 0x0FF).chr # deconstructing in IDA showed Microsoft LCG
  end
  return key
end

def decrypt(data, key)
  c = OpenSSL::Cipher.new('DES') # TODO key length shows it's DES
  c.decrypt
  c.key = key
  return (c.update(data) + c.final())
end

data = [IO.read("ELFhex").strip()].pack('H*') # ELFhex is the encoded file written out to a file using command 'xxd  -p -c 10000000 file.enc'

seed = 1575658800 #epoch time from december 6- 8 2019
until seed == 1575666000
  key = generate_key(seed)
  begin #need exception handling for else OpenSSL will quit if a bad decryption occurs
	  if decrypt(data, key)[0..3].to_s == "%PDF" #checks to see if decrypted file is PDF
	    puts("Found candidate")
	    puts("Generated key: #{key.unpack('H*')}")
	    new_data = decrypt(data, key)
	    File.open("#{seed}.pdf",'wb') do |f|
	    f.write(new_data) #writes pdf with seed value as name
	    end
	  end
	  seed += 1
  rescue
    seed += 1
  end
end
