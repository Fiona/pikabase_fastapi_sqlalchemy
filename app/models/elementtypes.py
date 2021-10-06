from sqlalchemy import Column, Integer, String, Table, ForeignKey, relationship

from app.db.base import Base


element_type_effectiveness_table = Table('element_type_effectiveness', Base.metadata,
    Column('left_id', ForeignKey('left.id'), primary_key=True),
    Column('right_id', ForeignKey('right.id'), primary_key=True)
)


class ElementType(Base):
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, index=True)
    name = Column(String, index=False)

    effectiveness = relationship(
        "ElementType",
        secondary=element_type_effectiveness_table)

    #effectiveness = models.ManyToManyField(
    #    "self",
    #    through="ElementTypeEffectiveness", through_fields=("element_a", "element_b"),
    #    symmetrical=False, related_name="+"
    #)

#class ElementTypeEffectiveness(models.Model):
#    AMOUNT_CHOICES = (
#        ("none", "No Effect"),
#       ("weak", "Not Very Effective"),
#        ("normal", "Normal"),
#        ("super", "Super Effective"),
#    )
#    element_a = models.ForeignKey(ElementType, on_delete=models.CASCADE, related_name="+")
#    element_b = models.ForeignKey(ElementType, on_delete=models.CASCADE, related_name="+")
#    amount_as_attacker = models.CharField(max_length=16, choices=AMOUNT_CHOICES, default="normal")
#    amount_as_defender = models.CharField(max_length=16, choices=AMOUNT_CHOICES, default="normal")
