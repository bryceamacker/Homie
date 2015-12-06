 -- create a server
    -- 30s time out for a inactive client
    sv=net.createServer(net.TCP, 30)   
    local pin = 4
    gpio.mode(pin, gpio.OUTPUT)

    -- server listen on 80, 
    -- if data received, print data to console,
    -- then send "hello world" to remote.
    sv:listen(5683,function(c)
      c:on("receive", function(c, pl) 
         if (pl == "H") then
          print(pl)
          gpio.write(pin, gpio.HIGH)
        end
         if (pl == "L") then
          print(pl)
          gpio.write(pin, gpio.LOW)
        end
      end)
      c:send("hello python")
    end)