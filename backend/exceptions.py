from fastapi import HTTPException


UsernameAlreadyTaken = HTTPException(
    status_code=400,
    detail="A user with this name already exists."
)

InvalidUserName = HTTPException(
    status_code=400,
    detail="No user with this name exists."
)


InvalidPermissions = HTTPException(
    status_code=401,
    detail="You do not have permission for this action."
)

class SchemaValidationError(Exception):
	status_code = 400
	detail = 'Schema Validation Error'
	http_exception = HTTPException(status_code=status_code, detail=detail)