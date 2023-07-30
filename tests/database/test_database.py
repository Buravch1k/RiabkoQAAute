import pytest


@pytest.mark.database
def test_database_connection(database):
    database.test_connection()


@pytest.mark.database
def test_check_all_users(database):
    users = database.get_all_users()
    print("Users:")
    for user in users:
        print(user)


@pytest.mark.database
def test_check_user_sergii(database):
    user = database.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update(database):
    database.update_product_qnt_by_id(1, 25)
    product_qnt = database.select_product_qnt_by_id(1)

    assert product_qnt == 25


@pytest.mark.database
def test_product_insert(database):
    database.insert_product(4, "печиво", "солодке", 30)
    product_qnt = database.select_product_qnt_by_id(4)

    assert product_qnt == 30


@pytest.mark.database
def test_product_delete(database):
    database.insert_product(99, "тестові", "дані", 999)
    database.delete_product_by_id(99)
    product_qnt = database.select_product_qnt_by_id(99)

    assert product_qnt == None


@pytest.mark.database
def test_detailed_orders(database):
    orders = database.get_detailed_orders()
    print("Orders:")
    for order in orders:
        print(order)

    # Check that total number of orders is 1
    assert len(orders) == 1

    # Check the structure of the data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"
