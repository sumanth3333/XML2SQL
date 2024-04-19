
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

module.exports = {getAwardByid};

