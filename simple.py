import os
from PIL import Image



# files_in_annotations=os.listdir('validation/Annotations')
# print(str(files_in_annotations[0])+' '+str(len(files_in_annotations)))
# absolute_path=os.path.dirname(os.path.realpath('__file__'))
# mel_list=[]
# nevus_list=[]
# for file_name in files_in_annotations:
#     file_path=os.path.join(absolute_path,'train\\Annotations\\'+file_name)
#     with open(file_path) as f:
#         data = f.read()
#         if 'melanoma' in data:
#             mel_list.append(file_name)
#         f.close()

# for file_name in files_in_annotations:
#     file_path=os.path.join(absolute_path,'train\\Annotations\\'+file_name)
#     with open(file_path) as f:
#         data = f.read()
#         if 'nevus' in data:
#             nevus_list.append(file_name)
#             mel_list.remove(file_name)
#         f.close()

# files_in_train=os.listdir('train')
# files_in_train.remove(files_in_train[0])

# for i in range(len(nevus_list)):
#     nevus_list[i]=nevus_list[i][:len(nevus_list[i])-3]

# for file_name in files_in_train:
#     file_path=os.path.join(absolute_path,'train\\'+file_name)
#     if file_name[:len(file_name)-3] in nevus_list:
#         print('hello ')
#         img=Image.open(file_path)
#         img.save(absolute_path+'\\melanoma\\{}'.format(file_name))
#         img.close()



def anotation_data_fun(directory1,name):
    # directory should be of Anotation folder
    annotation_data=[]
    anotation_list=os.listdir(directory1+'\\Annotations\\')
    for file_name in anotation_list:
        file_path=os.path.join(directory1+'\\Annotations\\'+file_name)
        with open(file_path) as f:
            data=f.read()
            if name in data:
                annotation_data.append(file_name)
            f.close()
    return annotation_data


def saving_file(directory,absolute_path,dir_to_be_create_name,list_data,anotation_data):
    for i in range(len(anotation_data)):
        anotation_data[i]=anotation_data[i][:len(anotation_data[i])-3]
    for file_name in list_data:
        file_path=os.path.join(directory,file_name)
        if file_name[:len(file_name)-3] in anotation_data:
            img=Image.open(file_path)
            img.save(absolute_path+'\\test_sorted\\{}'.format(dir_to_be_create_name)+'\\{}'.format(file_name))
            img.close()

absolute_path=os.path.dirname(os.path.realpath('__file__'))
name='nevus'
directory=absolute_path+'\\test'
li=os.listdir(directory)
li.remove(li[0])
annotation_data=anotation_data_fun(directory,name)
saving_file(directory,absolute_path,name,li,annotation_data)

#saving_file(directory,name,)


