villanyora = 25 #amper
halozati_fesz = 230 #volt
v_teljesitmeny = villanyora * halozati_fesz

print("25 A villanyóra 230 V hálózati feszültség mellett ", v_teljesitmeny, " W teljesítményt tud kiszolgálni.")

light = 30 #W
light_number = 5
air_con = 1500 #W
washing_machine = 1200 #W
iron = 2000 #W

already_used = light_number * light + air_con + washing_machine
teljes_aramkor = already_used + iron

print("Az eddigi teljesítmény:", already_used)
print("Vasalóvan a teljesítmény:", teljes_aramkor)
print("A megszakító lekapcsol:", v_teljesitmeny<=teljes_aramkor)
