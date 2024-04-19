const { query } = require('express');
const mysql = require('mysql');

const mysqlConnection = mysql.createConnection({
  port: 3306,
  user: 'root',
  password: 'root',
  database: 'NSF',
});

mysqlConnection.connect((err) => {
  if (err) {
    console.log('Failed to connect to MySQL database:', err);
  } else {
    console.log('Connected to MySQL database');

    // mysqlConnection.query('SELECT * FROM award', function(err, result) {
    //   if (err) {
    //     console.log(err);
    //   } else {
    //     console.log('Got product list');
    //   }
    // });
  }
});

function getAwards(callback) {
    mysqlConnection.query('SELECT * FROM info', function(err, result) {
      // mysqlConnection.query('select award.AwardID, award.MinAmdLetterDate, award.MinAmdLetterDate, award.AwardEffectiveDate, award.AwardExpirationDate, award.AwardTotalIntnAmount, award.AwardAmount, award.FUND_OBLG,award.AWDG_AGCY_CODE, award.FUND_AGCY_CODE, award.CFDA_NUM, award.AbstractNarration, award_instrument.Value, institution.Name, concat (institution.Name,' , ', institution.StreetAddress, ' , ' ,institution.StreetAddress2,', ', institution.CityName,', ', institution.StateCode,' ,', institution.CountryName, ' ,',institution.ZipCode,' ,', institution.PhoneNumber) as Address, institution.CONGRESSDISTRICT, institution.ORG_UEI_NUM, institution.ORG_PRNT_UEI_NUM, concat(investigator.FirstName,', ', investigator.LastName) as investigators_name, investigator.EmailAddress, investigator.RoleCode, program_officer.SignBlockName, program_element.Text, program_element.Code, program_reference.Code from award JOIN award_instrument ON award.AwardID=award_instrument.AwardID JOIN institution ON award_instrument.AwardID=institution.AwardID JOIN investigator ON institution.AwardID=investigator.AwardID JOIN program_officer ON investigator.AwardID=program_officer.AwardID JOIN program_element ON program_officer.AwardID=program_element.AwardID JOIN program_reference ON program_element.AwardID=program_reference.AwardID',  function(err, result) {
        if (err) {
      console.log(err);
    } else {
      console.log('Got award list');
    }
    callback(result);
  });
}

module.exports = {
  mysqlConnection: mysqlConnection,
  getAwards: getAwards,
};
// select award.AwardID, program_officer.SignBlockName, concat(investigator.FirstName,investigator.LastName) from award, program_officer,investigator;
//mysqlConnection.query('select award.AwardID, program_officer.SignBlockName, concat (investigator.FirstName,investigator.LastName)as name from award, program_officer,investigator', function(err, result) {
//

