def testUKSchedule():
    click("1385154985438.png")
    type("chrome\n")
    find("1385155434949.png")
    click("1385155445140.png")
    type("www.ukathletics.com\n")
    assert(exists("1385156142968.png"))
    hover("1385154820675.png")
    click("Untitled.jpg")
    assert(find("1385155549103.png").exists("1385156087323.png"))

testUKSchedule()
    