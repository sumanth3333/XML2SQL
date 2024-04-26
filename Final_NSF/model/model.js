
function getAwardByid(id, awardlist)
{
    
    for( let ad of awardlist)
    {
        if (id == ad.AwardID)
        {
            return ad;
        }
    }
}

function getAwardByPI(id, awardlist)
{
    
    for( let ad of awardlist)
    {
        if (id == ad.First_Investigator)
        {
            return ad;
        }
    }
}
function getAwardByIns(id, awardlist)
{
    
    for( let ad of awardlist)
    {
        if (id == ad.Name)
        {
            return ad;
        }
    }
}
module.exports = {getAwardByid, getAwardByPI, getAwardByIns};

