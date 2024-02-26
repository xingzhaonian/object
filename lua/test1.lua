#!/usr/local/bin/lua

local function sleep(n)
    if n > 0 then
       os.execute("ping -n " .. tonumber(n + 1) .. " localhost > NUL")
    else
       print(n..'')
    end
 end
 
 
 local function count_down(n)
     for i in pairs(n)   do
        sleep(1)
        print('wait...'..i)
     end
 end

 count_down({1, 2, 3, 4, 5})
