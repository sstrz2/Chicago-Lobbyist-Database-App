#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through
# the data tier.
#
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
    def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
        self._Lobbyist_ID = Lobbyist_ID
        self._First_Name = First_Name
        self._Last_Name = Last_Name
        self._Phone = Phone

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Phone(self):
        return self._Phone


##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
    def __init__(
        self,
        Lobbyist_ID,
        Salutation,
        First_Name,
        Middle_Initial,
        Last_Name,
        Suffix,
        Address_1,
        Address_2,
        City,
        State_Initial,
        Zip_Code,
        Country,
        Email,
        Phone,
        Fax,
        Years_Registered,
        Employers,
        Total_Compensation,
    ):
        self._Lobbyist_ID = Lobbyist_ID
        self._Salutation = Salutation
        self._First_Name = First_Name
        self._Middle_Initial = Middle_Initial
        self._Last_Name = Last_Name
        self._Suffix = Suffix
        self._Address_1 = Address_1
        self._Address_2 = Address_2
        self._City = City
        self._State_Initial = State_Initial
        self._Zip_Code = Zip_Code
        self._Country = Country
        self._Email = Email
        self._Phone = Phone
        self._Fax = Fax
        self._Years_Registered = Years_Registered
        self._Employers = Employers
        self._Total_Compensation = Total_Compensation

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def Salutation(self):
        return self._Salutation

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Middle_Initial(self):
        return self._Middle_Initial

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Suffix(self):
        return self._Suffix

    @property
    def Address_1(self):
        return self._Address_1

    @property
    def Address_2(self):
        return self._Address_2

    @property
    def City(self):
        return self._City

    @property
    def State_Initial(self):
        return self._State_Initial

    @property
    def Zip_Code(self):
        return self._Zip_Code

    @property
    def Country(self):
        return self._Country

    @property
    def Email(self):
        return self._Email

    @property
    def Phone(self):
        return self._Phone

    @property
    def Fax(self):
        return self._Fax

    @property
    def Years_Registered(self):
        return self._Years_Registered

    @property
    def Employers(self):
        return self._Employers

    @property
    def Total_Compensation(self):
        return self._Total_Compensation


##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
    def __init__(
        self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients
    ):
        self._Lobbyist_ID = Lobbyist_ID
        self._First_Name = First_Name
        self._Last_Name = Last_Name
        self._Phone = Phone
        self._Total_Compensation = Total_Compensation
        self._Clients = Clients

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Phone(self):
        return self._Phone

    @property
    def Total_Compensation(self):
        return self._Total_Compensation

    @property
    def Clients(self):
        return self._Clients


##################################################################
#
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
    sql = "Select count(*) from LobbyistInfo;"
    result = datatier.select_one_row(dbConn, sql)
    if result == None or len(result) == 0:
        return -1
    else:
        return result[0]


##################################################################
#
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
    sql = "Select count(*) from EmployerInfo;"
    result = datatier.select_one_row(dbConn, sql)
    if result == None or len(result) == 0:
        return -1
    else:
        return result[0]


##################################################################
#
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
    sql = "Select count(*) from ClientInfo;"
    result = datatier.select_one_row(dbConn, sql)
    if result == None or len(result) == 0:
        return -1
    else:
        return result[0]


##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and %
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID;
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#


# Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
def get_lobbyists(dbConn, pattern):
    sql = """
    SELECT Lobbyist_ID,First_Name,Last_Name,Phone
    FROM LobbyistInfo
    WHERE First_Name LIKE ? OR Last_Name LIKE ?
    ORDER BY Lobbyist_ID asc;
    """

    results = datatier.select_n_rows(dbConn, sql, [pattern, pattern])
    if results == None or len(results) == 0:
        return []
    else:
        return [Lobbyist(*row) for row in results]


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
    sql = """
   SELECT LobbyistInfo.*,SUM(Compensation_Amount)
   FROM LobbyistInfo
   LEFT JOIN Compensation ON LobbyistInfo.Lobbyist_ID = Compensation.Lobbyist_ID
   WHERE LobbyistInfo.Lobbyist_ID = ?;
   """

    info = datatier.select_one_row(dbConn, sql, [lobbyist_id])

    sql = """
   SELECT DISTINCT YEAR
   FROM LobbyistInfo
   JOIN LobbyistYears ON LobbyistInfo.Lobbyist_ID = LobbyistYears.Lobbyist_ID
   WHERE LobbyistInfo.Lobbyist_ID = ?;
   """

    data = datatier.select_n_rows(dbConn, sql, [lobbyist_id])
    years = []
    if data != None:
        for row in data:
            years.append(row[0])

    sql = """
   SELECT DISTINCT Employer_Name
   From LobbyistInfo
   JOIN LobbyistAndEmployer ON LobbyistAndEmployer.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
   JOIN EmployerInfo ON LobbyistAndEmployer.Employer_ID = EmployerInfo.Employer_ID 
   WHERE LobbyistInfo.Lobbyist_ID = ?
   ORDER BY Employer_Name;
   """

    data = datatier.select_n_rows(dbConn, sql, [lobbyist_id])
    names = []
    if data != None:
        for row in data:
            names.append(row[0])

    if info == None or info == () or info[0] == None:
        return None
    else:
        if info[-1] == None:
            comp = 0.00
        else:
            comp = info[-1]
        return LobbyistDetails(*info[:-1], years, names, comp)


##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid.
#          An empty list is also returned if an internal error
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
    sql = """
   SELECT LobbyistInfo.Lobbyist_ID,First_Name,Last_Name,Phone, SUM(Compensation_Amount)
   FROM LobbyistInfo
   JOIN Compensation ON LobbyistInfo.Lobbyist_ID = Compensation.Lobbyist_ID
   JOIN ClientInfo on Compensation.Client_ID = ClientInfo.Client_ID
   WHERE strftime("%Y",Compensation.Period_Start) = ?
   GROUP BY LobbyistInfo.Lobbyist_ID
   ORDER BY SUM(Compensation_Amount) desc
   LIMIT ?;
   """
    results = datatier.select_n_rows(dbConn, sql, [year, N])

    sql1 = """
   Select Distinct Compensation.Client_ID
   FROM LobbyistInfo
   JOIN Compensation ON LobbyistInfo.Lobbyist_ID = Compensation.Lobbyist_ID
   JOIN ClientInfo on Compensation.Client_ID = ClientInfo.Client_ID
   WHERE strftime("%Y",Compensation.Period_Start) = ? AND LobbyistInfo.Lobbyist_ID = ?;
   """

    sql2 = "Select Client_Name from ClientInfo where Client_ID = ?;"
    count = 0
    names = []
    for row in results:
        ids = datatier.select_n_rows(dbConn, sql1, [year, row[0]])
        names.append([])
        for idn in ids:
            names[count].append(datatier.select_one_row(dbConn, sql2, [idn[0]])[0])
        count += 1

    count = 0
    if results == None or len(results) == 0:
        return []
    else:
        rtn = []
        for row in results:
            rtn.append(LobbyistClients(*row, sorted(names[count])))
            count += 1
        return rtn
        # return [LobbyistClients(*row[:-1],sorted(row[-1].split('^'))) for row in results]


##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below),
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
    sql = """
   Select Lobbyist_ID
   FROM LobbyistInfo
   WHERE Lobbyist_ID = ?;
   """

    check = datatier.select_one_row(dbConn, sql, [lobbyist_id])
    if check == None or len(check) == 0:
        return 0
    else:
        sql = """
      INSERT INTO LobbyistYears(Lobbyist_ID, Year)
      VALUES (?,?);
      """
        count = datatier.perform_action(dbConn, sql, [lobbyist_id, year])

        if count == -1:
            return 0
        else:
            return 1


##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
    sql = """
   UPDATE LobbyistInfo
   SET Salutation = ?
   WHERE Lobbyist_ID = ?;
   """
    count = datatier.perform_action(dbConn, sql, [salutation, lobbyist_id])
    if count == 1:
        return 1
    else:
        return 0
