-- a udp server
s=net.createServer(net.TCP)
cu=net.createConnection(net.TCP)
s:on("receive",function(s,c)
	ip = c
	print(ip)
	-- Send Response 
	cu:on("receive",function(cu,c) print(c) end)
	cu:connect(5683,"192.168.2.115")
	cu:send("hello")
end)
s:listen(5683)