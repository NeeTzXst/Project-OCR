from PIL import Image, ImageEnhance

#read the image
room = '1101'
#im = Image.open("D:\project\hornai-50cm\hornai-50cm-"+room+".jpg")
im = Image.open("D:\Project OCR\Hornai-50\hornai-50cm-"+room+".jpg")
#image brightness enhancer
enhancer = ImageEnhance.Contrast(im)
factor = 1.5 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('D:\Project OCR\Addcon\hornai-50cm-300-addcont15-'+room+'.jpg')

factor = 2 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('D:\Project OCR\Addcon\hornai-50cm-300-addcont20-'+room+'.jpg')

factor = 2.5 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('D:\Project OCR\Addcon\hornai-50cm-300-addcont25-'+room+'.jpg')

factor = 3 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('D:\Project OCR\Addcon\hornai-50cm-300-addcont30-'+room+'.jpg')
"""
factor = 1.5 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('D:\project\hornai-50cm-addcont\contrast-15-hornai-50cm-'+room+'.jpg')

factor = 2 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('D:\project\hornai-50cm-addcont\contrast-20-hornai-50cm-'+room+'.jpg')

factor = 2.5 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('D:\project\hornai-50cm-addcont\contrast-25-hornai-50cm-'+room+'.jpg')

factor = 3 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('D:\project\hornai-50cm-addcont\contrast-30-hornai-50cm-'+room+'.jpg')
  """  
"""
factor = 1 #gives original image
im_output = enhancer.enhance(factor)
im_output.save('original-hornai-60cm-1101.jpg')

factor = 0.5 #decrease constrast
im_output = enhancer.enhance(factor)
im_output.save('less-contrast-hornai-60cm-1101.jpg')
"""