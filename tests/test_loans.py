import pytest

def test_create_loans_returns_201(client):
    response=client.post("/api/loans", json=loans_payload())
    assert response.status_code==201
    data-response.json()
    assert data["id"]==1 assert data["borrower_name"]=="..."

def test_duplicate_loans_returns_409(client):
    client.post("/api/loans", json=loans_payload())
    assert response.status_code==409
    assert "already exists" in resonse.json()
   
def loans_payload(
        id:ID1234567,
        equipment_id:"",
        borrower_name:"",
        loan_days:"",
        purpose:"",
):
    return{
        "equipment_id"=equipment_id,
        "borrower_name"=borrower_name,
        "loan_days"=loan_days,
        "purpose"=purpose,
        "id"=sid
    }