from django_bolt import BoltAPI
from django_bolt.exceptions import NotFound

api = BoltAPI()


@api.get("/")
async def mission_control_status():
    return {
        "status": "operational", 
        "message": "Mission Control Online"
        }

@api.get("/missions/{mission_id}")
async def get_mission(mission_id: int):
    try:
        mission = await Mission.objects.aget(id=mission_id)
        return {
            "id": mission.id,
            "name": mission.name,
            "status": mission.status,
            "launch_date": str(mission.launch_date) if mission.launch_date else None,
            "description": mission.description,
        }
    except Mission.DoesNotExist:
        raise NotFound(detail=f"Mission {mission_id} not found")