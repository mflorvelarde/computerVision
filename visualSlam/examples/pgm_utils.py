def pgm_load(filename):

    print('Loading image from file %s...' % filename)
    
    fd = open(filename, 'rt')
    
    # Skip constant header
    fd.readline()
    
    # Grab image size (assume square)
    imgsize = [int(tok) for tok in fd.readline().split()]
        
    # Start with empty list
    imglist = []
    
    # Read lines and append them to list until done
    while True:  
        
        line = fd.readline()
        
        if len(line) == 0:
            break       
            
        imglist.extend([int(tok) for tok in line.split()])   

    fd.close()
    
    # Convert list into bytes
    imgbytes = bytearray(imglist)     

    return imgbytes, imgsize
    
def pgm_save(filename, imgbytes, imgsize):    
    
    print('\nSaving image to file %s' % filename)
        
    output = open(filename, 'wt')
    
    output.write('P2\n%d %d 255\n' % imgsize)
    
    wid, hgt = imgsize
    
    for y in range(hgt):
        for x in range(wid):
            output.write('%d ' % imgbytes[y * wid + x])
        output.write('\n')

    output.close()

     
                                        
