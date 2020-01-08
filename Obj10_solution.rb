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


#data = ['714b08c1418896cd98dd1074c9733467'].pack('H*') #hex output from encoded file
#seed = 1578431515 #time seed

data = [IO.read("ELFhex").strip()].pack('H*')
#seed = 1578430989

seed = 1575658800
until seed == 1575666000
  key = generate_key(seed)
  puts seed
  begin
	  if decrypt(data, key)[0..3].to_s == "%PDF"
	    puts("Found candidate")
	    puts("Generated key: #{key.unpack('H*')}")
	    new_data = decrypt(data, key)
	    File.open("#{seed}.pdf",'wb') do |f|
	    f.write(new_data)
	    end
	  end
	  seed += 1
  rescue
    seed += 1
  end
end


