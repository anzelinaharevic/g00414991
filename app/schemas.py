from typing import Annotated

from pydantic import BaseModel

borrowers_nameStr=Annotated[str,StringConstraints(min_lenght=2), (max_lenght=60)]
loan_days:Field(gt=1,lt=14)
purposeStr=Annotated[str,StringConstraints(min_lenght=5), (max_lenght=100)]
idStr=" "[str,StringConstraints(pattern=r"^S\d{7}$")]
equipment_idStr=" "[str,StringConstraints(pattern=r"^S\d{7}$")]
status = PENDING