
from datetime import datetime
from bson import ObjectId

class SWOTAnalysis:
    def __init__(self, db):
        self.collection = db.swot_entries

    def create_analysis(self, strengths, weaknesses, opportunities, threats):
        entry = {
            "strengths": strengths,
            "weaknesses": weaknesses,
            "opportunities": opportunities,
            "threats": threats,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        return self.collection.insert_one(entry).inserted_id

    def get_analysis(self, analysis_id):
        return self.collection.find_one({"_id": ObjectId(analysis_id)})

    def update_analysis(self, analysis_id, data):
        data["updated_at"] = datetime.utcnow()
        return self.collection.update_one(
            {"_id": ObjectId(analysis_id)},
            {"$set": data}
        )

    def delete_analysis(self, analysis_id):
        return self.collection.delete_one({"_id": ObjectId(analysis_id)})
