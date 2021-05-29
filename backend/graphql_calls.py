
from graphene import ObjectType, Enum, ID, Int, List, NonNull, String, Schema

class BloodType(Enum):
    """Enum for blood type"""
    A = 1
    B = 2
    AB = 3
    O = 4

    @property
    def description(self):
        """Descriptions for each blood type enum"""
        if self == BloodType.A:
            return 'Blood type A'
        elif self == BloodType.B:
            return 'Blood type B'
        elif self == BloodType.AB:
            return 'Blood type AB'
        elif self == BloodType.O:
            return 'Blood type O'
        else:
            raise ValueError('Invalid blood type.')

class Query(ObjectType):
    """Personal profile of patient."""

    # Fields
    id_no = ID(description='Unique patient id for hospital records', required=True)
    blood_type = BloodType()
    vaccines = List(NonNull(String))
    bed_no = Int()
    room_no = Int()
    prescribed_rx = List(NonNull(String))
    doctor = String()

    # Resolvers
    def resolve_id_no(root, info):
        return 'dummy'

    def resolve_blood_type(root, info):
        return 'dummy'

    def resolve_vaccines(root, info):
        return 'dummy'

    def resolve_bed_no(root, info):
        return 'dummy'

    def resolve_room_no(root, info):
        return 'dummy'

    def resolve_prescribed_rx(root, info):
        return 'dummy'

    def resolve_doctor(root, info):
        return 'dummy'

query = '{ vaccines }'
schema = Schema(query=Query)
result = schema.execute(query)
print(result.data['vaccines'])
