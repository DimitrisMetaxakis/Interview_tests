from pages.spitogatos import SpitogatosUtilities


def test_basic_spitogatos_submit():
    # Given the Spitogatos home page is displayed
    b1 = SpitogatosUtilities()

    # When the user submits valid inputs in all fields of submission form
    b1.completeform("Dimitris", "Metaxakis", "+30 432564325", "Jim@spitogatos.com", "Hello everyone", True)

    # Then verify pop up shows "Success" message
    assert b1.success_message() == "Success"

    # Close browser
    b1.close_browser()


def test_invalid_spitogatos_submit():
    # Given the Spitogatos home page is displayed
    b1 = SpitogatosUtilities()

    # When the user submits invalid inputs in submission form
    b1.completeform("D1m1tr!s", "Met@x4k1s", "Fourtyseven23", "dfhdfefdtcom", None, False)

    # Then verify inline Error messages
    assert b1.warning_message_fName() == "The First Name may only contain letters."
    assert b1.warning_message_lName() == "The Last Name may only contain letters."
    assert b1.warning_message_mail() == "The Email must be a valid email address."

    # Bug : Inline error does not appear
    # assert b1.warning_message_phone() == "The Phone may contain only digits, spaces, and symbols"

    # Close browser
    b1.close_browser()


def test_only_optional_submit():
    # Given the Spitogatos home page is displayed
    b1 = SpitogatosUtilities()

    # When the user submits only optional inputs
    b1.completeform(None, None, None, "Jim@spitogatos.com", "Hello everyone", False)

    # Then verify inline Error messages
    assert b1.warning_message_fName() == "First Name field is required."
    assert b1.warning_message_lName() == "Last Name field is required."
    assert b1.warning_message_terms() == "Accept terms of use field is required."

    # Bug : Inline error does not appear
    # assert b1.warning_message_phone() == "The Phone is required"

    # Close browser
    b1.close_browser()


def test_only_required_submit():
    # Given the Spitogatos home page is displayed
    b1 = SpitogatosUtilities()

    # When the user submits only required inputs
    b1.completeform("Dimitris", "Metaxakis", "+30 432564325", None, None, True)

    # Then pop up shows "Success" message
    assert b1.success_message() == "Success"

    # Close browser
    b1.close_browser()


test_basic_spitogatos_submit()
test_invalid_spitogatos_submit()
test_only_optional_submit()
test_only_required_submit()
