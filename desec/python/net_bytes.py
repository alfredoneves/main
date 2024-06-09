#!/usr/bin/python3

some_bytes1 = """d4 ab 82 45 c4 0c 00 0c 29 76 43 e1 08 00 45 00
02 37 2c c0 40 00 40 06 77 32 c0 a8 00 0a 25 3b
ae e1 a9 fe 00 50 ff 4d 66 60 dd cb e4 96 80 18
00 e5 96 f8 00 00 01 01 08 0a f7 cb 2f 62 41 1c
2e df 50 4f 53 54 20 2f 69 6e 74 72 61 6e 65 74
2f 68 6f 6d 65 2e 70 68 70 20 48 54 54 50 2f 31
2e 31 0d 0a 48 6f 73 74 3a 20 77 77 77 2e 62 75
73 69 6e 65 73 73 63 6f 72 70 2e 63 6f 6d 2e 62
72 0d 0a 55 73 65 72 2d 41 67 65 6e 74 3a 20 4d
6f 7a 69 6c 6c 61 2f 35 2e 30 20 28 58 31 31 3b
20 4c 69 6e 75 78 20 78 38 36 5f 36 34 3b 20 72
76 3a 36 30 2e 30 29 20 47 65 63 6b 6f 2f 32 30
31 30 30 31 30 31 20 46 69 72 65 66 6f 78 2f 36
30 2e 30 0d 0a 41 63 63 65 70 74 3a 20 74 65 78
74 2f 68 74 6d 6c 2c 61 70 70 6c 69 63 61 74 69
6f 6e 2f 78 68 74 6d 6c 2b 78 6d 6c 2c 61 70 70
6c 69 63 61 74 69 6f 6e 2f 78 6d 6c 3b 71 3d 30
2e 39 2c 2a 2f 2a 3b 71 3d 30 2e 38 0d 0a 41 63
63 65 70 74 2d 4c 61 6e 67 75 61 67 65 3a 20 65
6e 2d 55 53 2c 65 6e 3b 71 3d 30 2e 35 0d 0a 41
63 63 65 70 74 2d 45 6e 63 6f 64 69 6e 67 3a 20
67 7a 69 70 2c 20 64 65 66 6c 61 74 65 0d 0a 52
65 66 65 72 65 72 3a 20 68 74 74 70 3a 2f 2f 77
77 77 2e 62 75 73 69 6e 65 73 73 63 6f 72 70 2e
63 6f 6d 2e 62 72 2f 69 6e 74 72 61 6e 65 74 2f
68 6f 6d 65 2e 70 68 70 0d 0a 43 6f 6e 74 65 6e
74 2d 54 79 70 65 3a 20 61 70 70 6c 69 63 61 74
69 6f 6e 2f 78 2d 77 77 77 2d 66 6f 72 6d 2d 75
72 6c 65 6e 63 6f 64 65 64 0d 0a 43 6f 6e 74 65
6e 74 2d 4c 65 6e 67 74 68 3a 20 33 38 0d 0a 44
4e 54 3a 20 31 0d 0a 43 6f 6e 6e 65 63 74 69 6f
6e 3a 20 6b 65 65 70 2d 61 6c 69 76 65 0d 0a 55
70 67 72 61 64 65 2d 49 6e 73 65 63 75 72 65 2d
52 65 71 75 65 73 74 73 3a 20 31 0d 0a 0d 0a 75
73 65 72 6e 61 6d 65 3d 6a 6f 69 6e 76 69 6c 6c
65 26 70 61 73 73 77 6f 72 64 3d 4a 25 32 35 31
33 34 35 6b 39"""
    
some_bytes = "d4 ab 82 45 c4 0c 00 0c 29 76 43 e1 08 00 45 00 00 4c d1 b4 00 00 40 01 4e a3 ac 10 01 37 ac 10 01 02 08 00 dc 3a 83 08 00 00 64 73 74 20 68 74 74 70 20 70 6f 72 74 20 38 30 20 2f 6d 61 6c 77 61 72 65 2e 74 78 74 20 2d 20 4b 45 59 3a 20 30 30 32 39 38 34 31 37 31 37 32"
    
class Net_bytes:
	def __init__(self, src_mac=None, dst_mac=None, the_type=None, version=None, ihl=None, type_of_service=None,
			  total_length=None, id_flags_frag=None, ttl=None, protocol=None, h_checksum=None, src_addr=None,
			  dst_addr=None, src_port=None, dst_port=None, sqn_ack_number=None, tcp_flags=None):
		self.src_mac = src_mac
		self.dst_mac = dst_mac
		self.the_type = the_type
		self.version = version
		self.ihl = ihl	# I will consider it as 5 in the analysis, this will exclude options and padding!!!
		self.type_of_service = type_of_service
		self.total_length = total_length
		self.id_flags_frag = id_flags_frag
		self.ttl = ttl
		self.protocol = protocol
		self.h_checksum = h_checksum
		self.src_addr = src_addr
		self.dst_addr = dst_addr
		self.src_port = src_port
		self.dst_port = dst_port
		self.sqn_ack_number = sqn_ack_number
		self.tcp_flags = tcp_flags
	
	def receive_bytes(self, string_bytes):
		"""
			Receive a string with the network bytes and transform it in a clean list
		"""
		bytes_list = []
		
		for string in string_bytes.split(" "):
			# Split the string by '\n' and extend the modified_list
			bytes_list.extend(string.split('\n'))
		
		self.dst_mac = " ".join(bytes_list[:6])
		self.src_mac = " ".join(bytes_list[6:12])
		self.the_type = " ".join(bytes_list[12:14])
		
		if self.the_type == "08 00":	# IP
			self.version = " ".join(bytes_list[14:15])[0]
			self.ihl = " ".join(bytes_list[14:15])[1]
			self.type_of_service = " ".join(bytes_list[15:16])
			self.total_length = " ".join(bytes_list[16:18])
			self.id_flags_frag = " ".join(bytes_list[18:22])
			self.ttl = " ".join(bytes_list[22:23])
			self.protocol = " ".join(bytes_list[23:24])
			self.h_checksum = " ".join(bytes_list[24:26])
			self.src_addr = " ".join(bytes_list[26:30])
			self.dst_addr = " ".join(bytes_list[30:34])
			self.src_port = " ".join(bytes_list[34:36])
			self.dst_port = " ".join(bytes_list[36:38])
			self.sqn_ack_number = " ".join(bytes_list[38:46])	# I removed the 2 bytes from reserved
			self.tcp_flags = " ".join(bytes_list[46:47])

	def print_all(self):
		print(f"dst_mac = {self.dst_mac}")
		print(f"src_mac = {self.src_mac}")
		print(f"type = {self.the_type}")
		
		if self.the_type == "08 00":
			print(f"version = {self.version}")
			print(f"ihl = {self.ihl}")	
			print(f"type of service = {self.type_of_service}")
			print(f"total length = {self.total_length}")
			print(f"id, flags, frag = {self.id_flags_frag}")
			print(f"ttl = {self.ttl}")
			print(f"protocol = {self.protocol}")
			print(f"header checksum = {self.h_checksum}")
			print(f"source address = {self.src_addr}")
			print(f"destination address = {self.dst_addr}")
			print(f"source port = {self.src_port}")
			print(f"destination port = {self.dst_port}")
			print(f"sequence, ack number, data_offset = {self.sqn_ack_number}")
			print(f"TCP flags = {self.tcp_flags}")

		
nb = Net_bytes()	# instance the class
nb.receive_bytes(some_bytes)
nb.print_all()



