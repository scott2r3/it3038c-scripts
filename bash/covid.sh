DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
HOSPITAL=$(echo $DATA | jq '.[0].hospitalizedCurrently')
ICU=$(echo $DATA | jq '.[0].inIcuCurrently')
VENTCURRENT=$(echo $DATA | jq ' .[0].onVentilatorCurrently')
DEATH=$(echo $DATA | jq '.[0].death')

TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, $HOSPITAL people that are hospitalized currently, $ICU in ICU currently, $VENTCURRENT on ventilators currently and $DEATH deaths."
