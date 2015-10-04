-- a udp server
s=net.createServer(net.UDP)
cu=net.createConnection(net.UDP)
s:on("receive",function(s,c)
	ip = c
	print(ip)
	-- Send Response 
	cu:on("receive",function(cu,c) print(c) end)
	cu:connect(5683,"192.168.1.119")
	cu:send("hello")
end)
s:listen(5683)
