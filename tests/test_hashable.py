from core.hashtable import HashTable

def test_should_create_hastable():
    assert HashTable(capacity=100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100