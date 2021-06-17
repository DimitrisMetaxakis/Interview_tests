from pages.sgdigital import SgdigitalUtilities


def test_invalid_sgdigital_submit():
    # Given the Sgdigital contact page is displayed
    b1 = SgdigitalUtilities()

    # When the user submits invalid inputs in submission form
    b1.completeform("2109626143", "6980520201504$$$$$$", "Fourtyseven23", "dfhdfefdtcom", "2662585448655")

    # Then verify inline Error messages
    assert b1.warning_message_mail() == "Please enter a valid email address."

    # Bug 1 : Inline error does not appear in name
    # assert b1.warning_message_name() == "Please enter a valid name"
    # Bug 2 : Inline error does not appear in phone
    # assert b1.warning_message_phone() == "Please enter a valid phone number"

    # Close browser
    b1.close_browser()


def test_mandatory_sgdigital_submit():
    errormessage = "This field is required."
    # Given the Sgdigital contact page is displayed
    b1 = SgdigitalUtilities()

    # When the user submits only optional inputs
    b1.completeform(None, None, "+30 6980520201", None, None)

    # Then verify inline Error messages
    assert b1.warning_message_name() == errormessage
    assert b1.warning_message_mail() == errormessage
    assert b1.warning_message_company() == errormessage
    assert b1.warning_message_message() == errormessage

    # Bug : Inline error does not appear
    # assert b1.warning_message_phone() == "The Phone is required"

    # Close browser
    b1.close_browser()


test_invalid_sgdigital_submit()
test_mandatory_sgdigital_submit()
