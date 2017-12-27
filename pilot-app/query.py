from mlab import mlab_connect
from models.service import Service

mlab_connect()

all_female_services = Service.objects(gender=0, height__gte=160)

for female_service in all_female_services:
    print(female_service)

first_female_160 = Service.objects(gender=0, height__gte=160).first()

avail_f_160 = Service.objects(gender=0, height__gte=160, occupied=False).first()
if avail_f_160 is None:
    print("Not found")
else:
    avail_f_160.update(set__occupied=True)
    avail_f_160.reload()
    print(avail_f_160)

# id_to_find = "5a3e7a69f90633c35c6a37d4"
# # jess = Service.objects(id=id_to_find).first() # regular
# laura = Service.objects().with_id(id_to_find) #id only
# if laura is None:
#     print("Not found")
# else:
#     print(laura.name)
#     # laura.delete
#     laura.update(set__occupied=True) # inc__
#     laura.reload()
#     print(laura.occupied)



# all_services = Service.objects()
#
# for service in all_services:
#     print(service.name)
