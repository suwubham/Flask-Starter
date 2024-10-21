from app.extensions import db


class Country(db.Model):
    __tablename__ = 'Country'
    country_id = db.Column(db.String(), primary_key=True)
    country_name = db.Column(db.String(), nullable=False)
    country_code = db.Column(db.String(), nullable=False)
    states = db.relationship('State', backref='Country', lazy=True)


class State(db.Model):
    __tablename__ = 'State'
    state_id = db.Column(db.String(), primary_key=True)
    state_name = db.Column(db.String(), nullable=False)
    country_id = db.Column(db.String(), db.ForeignKey(
        'Country.country_id'), nullable=False)
    districts = db.relationship('District', backref='State', lazy=True)


class District(db.Model):
    __tablename__ = "District"
    district_id = db.Column(db.String(), primary_key=True)
    district_name = db.Column(db.String(), nullable=False)
    state_id = db.Column(db.String(), db.ForeignKey(
        'State.state_id'), nullable=False)
    municipalities = db.relationship(
        'Municipality', backref='District', lazy=True)


class Municipality(db.Model):
    __tablename__ = 'Municipality'
    municipality_id = db.Column(db.String(), primary_key=True)
    municipality_name = db.Column(db.String(), nullable=False)
    district_id = db.Column(db.String(), db.ForeignKey(
        'District.district_id'), nullable=False)
