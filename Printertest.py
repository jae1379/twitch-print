import printer, textwrap 

p=printer.ThermalPrinter(serialport="/dev/ttyAMA0") 
wrapped_text = textwrap.fill("\nHello Geek Gurl Diaries viewers!What happens if we try to print a longer sentence or paragraph? Will it go over multiple lines or will the text just be cut off? It's good to test these things you know!\n") 
p.print_text(wrapped_text) 
p.linefeed()
p.linefeed() 
p.linefeed()
