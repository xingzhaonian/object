local function sleep(n)
    if n > 0 then
       os.execute("ping -n " .. tonumber(n + 1) .. " localhost > NUL")
    else
       print(n..'')
    end
 end
 
 
 local function count_down(n)
     for i = n, 1, -1
    do
        sleep(1)
        print('ddd'..i..'dd')
     end
 end
 
 
 count_down(5)
 