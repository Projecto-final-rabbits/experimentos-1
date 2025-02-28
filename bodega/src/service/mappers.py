from src.shared.domain.repository import DomainMapper
from src.shared.application.mappers import ApplicationMapper
from src.domain.models import Product

from .dtos import ProductDTO

class ProductMapperDtoJson(ApplicationMapper):
    def extern_to_dto(self, externo: dict):
        product_dto = ProductDTO()

        return product_dto
    
    def dto_to_extern(self, dto: ProductDTO):
        return dto.__dict__
        

class ProductMapper(DomainMapper):
    def entity_to_dto(self, obj: Product) -> ProductDTO:
        return obj

    def dto_to_entity(self, obj: ProductDTO) -> Product:
      product = Product()
      product.name = obj['name']

      return product  

    def get_type(self):
        return Product.__class__