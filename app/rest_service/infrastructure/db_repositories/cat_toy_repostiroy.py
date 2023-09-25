from sqlalchemy.orm import Session

class CatToyRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, cat_toy: CatToy):
        self.db_session.add(cat_toy)
        self.db_session.commit()
        self.db_session.refresh(cat_toy)
        return cat_toy

    def get_all(self):
        return self.db_session.query(CatToy).all()

    def get_by_id(self, cat_toy_id: int):
        return self.db_session.query(CatToy).filter(CatToy.id == cat_toy_id).first()

    def update(self, cat_toy: CatToy):
        self.db_session.merge(cat_toy)
        self.db_session.commit()
        self.db_session.refresh(cat_toy)
        return cat_toy

    def delete(self, cat_toy: CatToy):
        self.db_session.delete(cat_toy)
        self.db_session.commit()