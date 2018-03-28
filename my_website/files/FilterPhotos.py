import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os
import os.path  
import PIL.ImageDraw  
import PIL.ImageFilter  
import PIL.Image  
import PIL.ImageFont
import textwrap          

def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def frame_image(original_image, wide=15):
    
    #Looks for a folder named "Results" and makes it if it's not there
    directory = os.getcwd()
    new_directory = os.path.join(directory, 'Results')
    try:
        os.mkdir(new_directory)
    except:
        pass
    
    #Gets images from the directory and reserves their size
    image_list, file_list = get_images(directory)
    width, height = original_image.size
    
    #Adds the frame on a photo
    frame = PIL.Image.new('RGBA', (width, height), (0,0,0,0))
    drawing_layer2 = PIL.ImageDraw.Draw(frame)
    drawing_layer2.rectangle([(width/wide,height/wide), ((width/wide)*(wide-1),(height/wide)*(wide-1))],fill=(184,2,2,255))
    result = PIL.Image.new('RGBA', original_image.size, (184,2,2,255))
    result.paste(original_image,(0,0),mask=frame)
    
    #Adds the crest over the frame
    crest_img = PIL.Image.open('Crest.png')
    crest_small = crest_img.resize((height/wide, height/wide)) # w and h measured in plt
    result.paste(crest_small, (((width/2) - (width/wide/2)), 0))
    
    #Tells about the status of each photo as it's framed
    print 'Framing Image...'
    print 'Image',original_image,'has been framed.'
    return result
  
def frame_all_images(directory=None):
    
    #Looks for a folder named "Results" and makes it if it's not there
    if directory == None:
        directory = os.getcwd() 
    new_directory = os.path.join(directory, 'Results')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass  
        
    #Gets images from the directory and reserves their size
    image_list, file_list = get_images(directory)  
    
    # Go through the images and save modified versions
    for n in range(len(image_list)):
        
        # Parse the filename
        print n
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = frame_image(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '_framed' + '.png')
        new_image.save(new_image_filename)
    
    #Gives acknowledgement when all computers are framed
    print 'Success! All images have been framed!'