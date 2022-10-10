from Coordinate import Coordinate
from Quadrant import Quadrant


def test_should_get_quadrant_coordinate():
    # Arrange / Setup
    quadrantFirst = Quadrant(Coordinate(10, 20))
    quadrantFourth = Quadrant(Coordinate(3, -2))
    quadrantThird = Quadrant(Coordinate(-8, -1))
    quadrantSecond = Quadrant(Coordinate(-7, 1))
    quadrantNull = Quadrant(Coordinate(0, 1))

    # Act / Action
    resultFirst = quadrantFirst.get_quadrant_coordinate()
    resultFourth = quadrantFourth.get_quadrant_coordinate()
    resultThird = quadrantThird.get_quadrant_coordinate()
    resultSecond = quadrantSecond.get_quadrant_coordinate()
    resultNull = quadrantNull.get_quadrant_coordinate()

    # Assert
    assert resultFirst == "First"
    assert resultFourth == "Fourth"
    assert resultThird == "Third"
    assert resultSecond == "Second"
    assert resultNull == ""
