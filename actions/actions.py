import requests
import json
from rasa_sdk import Action


class ActionJoke(Action):
    def name(self):
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        request = requests.get('http://api.icndb.com/jokes/random').json()  # make an api call
        joke = request['value']['joke']  # extract a joke from returned json response
        dispatcher.utter_message('Here is a joke to cheer you up!')
        dispatcher.utter_message(joke)  # send the message back to the user
        return []


class ActionCoronaAbout(Action):
    def name(self):
        return "action_corona_about"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'First of all, No Need to be panic. People need not be afraid. It is not deadly virus. Mortality rate is 2-3%.  It is a virus family. First it was caused by the corona virus SARS corona virus and there was another outbreak which we call MERS CORONA virus which happened in middle east So it is a virus. There is a novel virus that has jumped from animal to human & animal virus converted into human virus, which has the ability to spread human to human. Some viruses jump species, but not spread human to human by air , this virus have such ability.')
        return []


class ActionCoronaWho(Action):

    def name(self):
        return "action_corona_who"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('W.H.O called it CORONA VIRUS. W.H.O declared it as Epidemic or Panidemic.')
        return []


class ActionCoronaSymptoms(Action):

    def name(self):
        return "action_corona_symptoms"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Current symptoms reported for patients with CORONA VIRUS have included mild to severe respiratory illness with fever1, cough, and difficulty breathing.')
        dispatcher.utter_message(
            'The Symptoms are normal like the symptoms of a common flu for  example fever, cold, sore throat, cough. These are also the symptoms of Corona virus but the second link with this is that if you travel and you have come from areas where outbreak of Corona virus has happened or if you have come in close contact (1-3 feet) of corona infected person or  you have touch  infected surface than have touch your face or eyes then needs to be investigated or test.')
        return []


class ActionCoronaIncubation(Action):

    def name(self):
        return "action_corona_incubation"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'This is called Incubation Period. Symptoms normally appears in 2-7 days in most patients and can varied up to max  in 10-14 days.')
        return []


class ActionCloseContact(Action):

    def name(self):
        return "action_close_contact"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Corona virus is a droplets infection. Suppose I have a corona virus infection. The viruse in my throat is multiplying rapidly. When I cough, the corona virus droplets come into the air. If I cough without protection, the corona virus droplets can go up to 1 or 2 meters at most.')
        dispatcher.utter_message(
            'So the virus will remain in the air inside this distance and uninfected person  come in close contact  within that 1 or 2 meters distance of that coughing person, then on breathing, the virus also enters inside with air.')
        dispatcher.utter_message(
            'There is another medium that someone has corona virus and he/she put their hand on mouth ,face or eyes, then the virus comes in his/her hands, now if he/she touch any surface like chair, door lock, door etc.  then that virus also comes on that surface.')
        dispatcher.utter_message(
            'If someone who is not infected from Corona virus touches that surface than that Virus also comes on his/her hand  and then does not wash hands with soap or sanitizer and in such a habit that if he/she  put his/her hands on nose or mouth or eyes, then there is a chance of them getting infected with corona virus.')
        return []


class ActionWrongSpread(Action):

    def name(self):
        return "action_corona_close"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Many people think that there is a case of corona virus in my colony, then they think that whole colony will infected from Corona Virus . But it  will not happen in the whole colony unless you don’t come in close contact with infected person and don’t take precautions.')
        dispatcher.utter_message(
            'If you come to the close contact of that corona infected person and you breathe or you touch infected surface , then you have a chance of getting infected with the corona.')
        return []


class ActionStayThings(Action):

    def name(self):
        return "action_stay_things"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'There is no method that you can detect about infection of surface from Corona Virus. So Only You have to take precautions & you should wash your hands with sanitizer & soap in every 15-30 minutes properly because you don’t know about surface & where you have touch your hands.')
        return []


class ActionRisky(Action):

    def name(self):
        return "action_risky"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Older patients and individuals who have severe underlying medical conditions or are immune compromised should contact their healthcare provider early, even if their illness is mild.Only few person either they are older means over 60 or child which have less immunity.')
        dispatcher.utter_message(
            'Those person having Blood Pressure, Heart Problem, Lungs Problem, Diabetes , Less Immunity ,there are chances in them that this virus which is in the throat, it will go down and reach the lungs and will cause viral pneumonia, which will cause you to have shortness of breath, oxygen will start, cough will come more, then these people will required ventilators. Due to secondary infection causing acute respiratory distress syndrome which can lead to death.')
        return []


class ActionInfectedPrecautions(Action):

    def name(self):
        return "action_infected_precautions"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'The one who has an infection with the corona, he/she should be an  honest and loyal to citizens of our country and should have  feeling that someone else should not infected because of me. For this, a person who has a cold should isolate himself, should home quarantined, should not go to any crowded place. If he go than put  a mask. If you have no mask then cover the cough with a tissue or handkerchief so that the droplets do not spread further and if there is no tissue then cough on the side of your shirt and wash your hands regularly.')
        dispatcher.utter_message(
            ' If child is infected in family, don’t send it to school or park or for play . Call Help Line Number ,They will take your sample from your home .If it seems emergency symptoms than Contact to Doctor & get Admitted & take necessary measures prescribed by doctor.')
        return []


class ActionHomeQuarantined(Action):

    def name(self):
        return "action_home_quarantined"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Meaning when you are infected or you see the symptoms then you keep yourself at home. Keep yourself confined to one room of the house, in which only you can keep more distance from people who are not infected. Avoid close contacts, wash hands regularly, use your mask, take paracetamol and good hydration.')
        return []


class ActionTestPositive(Action):

    def name(self):
        return "action_test_positive"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'No, it is necessary until you have emergency cases or you have problem of diabetes , blood pressure etc. But as a precaution so that the family does not have any problems from you and for  better quarantined , then you should admit yourself in isolation center which are open government hospital or many places or in ITBP Camp.')
        return []


class ActionVaccineAvailable(Action):

    def name(self):
        return "action_test_positive"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'No , recently there is no vaccine developed . If it will be developed than it will take 9-10 month to come in market because mass production, testing will be done which will take time. The Body’s Immunity is the solution or treatment of Corona Virus. Your Body fight with Corona Virus. Only few person either they are older means over 60 or child which have less immunity.')
        dispatcher.utter_message(
            'Those person having Blood Pressure, Heart Problem, Lungs Problem, Diabetes , Less Immunity ,there are chances in them that this virus which is in the throat, it will go down and reach the lungs and will cause viral pneumonia, which will cause you to have shortness of breath, oxygen will start, cough will come more, then these people will required ventilators. Due to secondary infection causing acute respiratory distress syndrome which can lead to death.')
        return []


class ActionMythVaccine(Action):

    def name(self):
        return "action_myth_vaccine"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'No, It Cannot Be Cured With Those Medicines. This Is A New Virus, A New Vaccine Will Have To Be Developed.')
        return []


class ActionRecurCorona(Action):

    def name(self):
        return "action_recur_corona"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'This thing decide by your immunity .Right now it is spreading because there is no immunity in the society. Even then, the chances remain low because the body immunity or Antibody  has been developed, &  if you get exposure to Corona Virus later on , even you get wild infection but you have mild symptoms now & it will be cured soon.')
        return []


class ActionPregnantChild(Action):

    def name(self):
        return "action_pregnant_child"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Data are not available, yet researched a pregnant woman who was infected &  found that the chances are negligible. But it has been observed that if this infection is severe or in emergency state in woman than chances of abortion or Uterus Infection rises.')
        dispatcher.utter_message(
            'We still do not know if a pregnant woman with Corona Virus can pass the virus that causes Corona Virus to her fetus or baby during pregnancy or delivery. No infants born to mothers with CORONA Virus have tested positive for the Corona virus.')
        dispatcher.utter_message(
            'In these cases, which are a small number, the virus was not found in samples of amniotic fluid or breastmilk.No infants born to mothers with Corona virus have tested positive for the Corona virus. In these cases, which are a small number, the virus was not found in samples of amniotic fluid or breastmilk.')
        return []


class ActionTestingCenters(Action):

    def name(self):
        return "action_testing_centers"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'No , Only Govt. approved Labs & some private Labs are allowed for Testing.Because sample taken ,transportation & storage process have a unique way.')
        return []


class ActionCoronaSurvive(Action):

    def name(self):
        return "action_corona survive"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Normally in  cold temperature, it lasts for 8-10 hours, but in summer it will only last for 1 to 2 hours. It depend on surfaces . On Cardboard it survive for 1-2 hours. On metal Surfaces with low temperature it can survive for 8-10 hours.')
        dispatcher.utter_message(
            'However according to W.H.O there is no established correlation between the variations in temperature and spread of Corona Virus. Since virus stays on surfaces for long  hours. So wash hands properly.')
        return []


class ActionCoronaGoods(Action):

    def name(self):
        return "action_corona_goods"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'No, it takes a few days to 1 week to pack up the goods coming from China and reach India, so even if those viruses are present on that stuff, they will either die or die on the way.')
        return []


class ActionAnimalInfection(Action):

    def name(self):
        return "action_animal_infection"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'These viruses originate from the meat market of China, there are seafood markets in China where there are live animals and they are not dead and in them, if the corona virus is in an animal like in a bat, pengulin etc  then that virus can mutate.')
        dispatcher.utter_message(
            'So that human virus and animal virus combined to become a new virus that can spread  human to  human .But now it has become a human virus, it has no relation with  vegetarian or non-vegetarian food . Also, as a precaution, if you want to eat non vegetarian food, then you should cook it well and eat it.')
        return []


class ActionJoke(Action):

    def name(self):
        return "action_name"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('')
        return []


class ActionWashHands(Action):

    def name(self):
        return "action_wash_hands"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'When we wash hands, do full steps so that the virus does not come in hand. Many people think that washing the hands in 2-3 minutes remove  the corona virus, but they are wrong, it remains on hand at some places. So wash hand  with soap or sanitizer & rub it well.')
        dispatcher.utter_message(
            'After that the back part of the hand specially  between the fingers, apply soap or sanitizer properly in it and clean it well. If left in the nails, apply soap or sanitizer to the nails and wash it well. Cleaned the thumb too. Then apply soap or sanitizer to the wrist in the last and rub it well. This process takes 2-3 minutes.')
        return []


class ActionTimeWash(Action):

    def name(self):
        return "action_time_wash"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'If we are out then we should do it every 6-7 hours. People who have infections like cough,cold & they are putting their hands on nose, mouth ,face repeatedly, they keep washing in 1-2 hours. Normally it is our habit that we keep our hands in our nose while talking, avoid it.')
        return []


class ActionJoke(Action):

    def name(self):
        return "action_name"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('')
        return []


class ActionMaskWear(Action):

    def name(self):
        return "action_mask_wear"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'See, as the corona virus can only spread within a radius of 1 or 2 meters, there is no need to put on a mask if we are walking in an open environment. But if we are going to the crowded area where we feel that we will not be able to save ourselves from getting infected then he can put 3 tripellate surgical masks.')
        dispatcher.utter_message(
            'As you are healthy , if you touch surface that is infected from Corona virus than by habit , he/she will readjust mask. In this process it become danger that you have chance of infected.')
        dispatcher.utter_message(
            'The common man who has a cough and he don’t want that it spread to others, then he can put 3 tripellate surgical masks. If you feel that there is a corona infected person in your home, then the person who has the infection and as a precaution should also apply the mask.')
        dispatcher.utter_message(
            'Health workers usually stay in close contact of patients, then they should use N95 masks goggles so that there will be no  infection. N 95 can filter small particulates matters like 2.5 by 90% .')
        return []


class ActionMaskChange(Action):

    def name(self):
        return "action_mask_change"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Normally the mask should be changed when wet or if you wash your hands with the mask then change it.')
        return []


class ActionColleauge(Action):

    def name(self):
        return "action_colleauge"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'In this you start a  process which is called Self Quarantined. Because you could get infection or you could also be source of transmitting it to other colleagues. If you have sitting with him, you have to attend meeting with him, you have to come in contact in 1-2 meter than you should have to be Self Quarantined. If you notice symptoms, report it to authority & test it.')
        return []


class ActionHospitalsInfected(Action):

    def name(self):
        return "action_hospitals_infected"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'It is safe to visit such hospitals that have isolation centers which are very far from OPD or other wards or other areas.Unless it is essential, avoid visit such hospitals for routine check up or non essential conditions that are crowded.')
        return []


class ActionTemperature(Action):

    def name(self):
        return "action_temperature"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'However according to W.H.O there is no established correlation between the variations in temperature and spread of Corona Virus.')
        dispatcher.utter_message(
            'This time it is not said as data is not available. But W.H.O have defined that it will survive in rising temperature . But with rising temperature , its transmissibility will decrease.')
        dispatcher.utter_message(
            'According to AIIMS Doctor , Temperature will not effect on it so much because of two reasons : First , We still have large number of cases in Singapore or Thialand ,these are tropical countries where temperature is over 30 . Secondly in Summer , In House, Malls and many places, Air Conditioner start. So it will survive in Indoor Conditions.')
        return []


class ActionAvoidMalls(Action):

    def name(self):
        return "action_avoid_malls"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Start Social Distancing Process . Avoid going to crowded places, big  functions unless it is essential.')
        return []


class ActionSocialDistancing(Action):

    def name(self):
        return "action_social_distancing"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Yes,This fact is  Correct . UK is following . UK allowed the infection to spread to the community but protect higher risk group that is elderly persons or persons having Blood Pressure, Diabetes , Heart Problem & those  have less immunity.')
        dispatcher.utter_message(
            'Mortality in younger age group is very low , you may have large number of individuals those who make at the infections and cause Heard Immunity & therefore you may not have very large outbreak.')
        return []


class ActionYoga(Action):

    def name(self):
        return "action_yoga"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'No, There is no evidence that Ayurvedic Medicine ,Tulsi, Garlic, Cow Urine, Onion,Yoga, Pranayam other drugs are effected for treatment of Corona Virus.')
        return []


class ActionBloodDonor(Action):

    def name(self):
        return "action_blood_donor"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Blood Donors does not required to be screened . But chances of being significantly present in Blood is nearly nil or very low.')
        return []


class ActionDrinkHot(Action):

    def name(self):
        return "action_drink_hot"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'No, Because when this virus enter in body .It remain present in Cells. I will not in Throat . It does not die with Hot Water. Hot Water leads to hydration that helps in improving immunity.')
        return []


class ActionSoapSanitizers(Action):

    def name(self):
        return "action_soap_sanitizers"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'If you wash hand with water than it is better than sanitizer. Because if you wash hand with soap you do properly and your completely hand as you rub it on your palm, on your fingers & nails . So all get washed like fingers , nails etc due to its foam.')
        dispatcher.utter_message(
            'But if you use sanitizer than you normally rub palm only. So virus can remain on nails, or between fingers. But if are out of home , or in travel & sanitizer is not available than you can use sanitizers but please wash properly the nails, fingers ,wrist & thumb along palm.')
        return []


class ActionCleanDoor(Action):

    def name(self):
        return "action_clean_door"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Yes , Because if a person having infection of Corona Virus and if he/she cough & touch door knobs than droplets will stay on door knobs for few hours. So if another person who don’t have Corona virus infection touch the door than touch his/her face or eyes than he/she will also infected.')
        dispatcher.utter_message(
            'So Cleaning the door knob with sanitizers is best. If you touch Door knobs , wash your hands properly.')
        return []


class ActionClothInfection(Action):

    def name(self):
        return "action_cloth_infection"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'If you touch clothes on which droplets fall & than you touch face & nose & eyes of self or others than it may chance of infection. So keep Hand Washing Properly  and avoid touching of your face and mouth.')
        return []


class ActionPrecautionPregnant(Action):

    def name(self):
        return "action_precaution_pregnant"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'There is no data. Pregnant woman have to take extra precautions . Pregnant women should do the same things as the general public to avoid infection. You can help stop the spread of CORONA VIRUS by taking these actions:')
        dispatcher.utter_message(
            'Cover your cough (using your elbow is a good technique).Avoid people who are sick.Clean your hands often using soap and water or alcohol-based hand sanitizer.')
        return []


class ActionFlight(Action):

    def name(self):
        return "action_flight"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Avoid crowded place unless essential. But if essential regular hand washing and other precautions to be taken. Use mask.')
        return []


class ActionImmunityIndians(Action):

    def name(self):
        return "action_immunity_indians"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'There is no data. During Swine Flu & H1 N1 Influenza have huge number of cases  and became epidemic in our country.')
        return []


class ActionSmoking(Action):

    def name(self):
        return "action_smoking"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Smoking leads to lungs problems and cause decrease in respiratory defence mechanism. Therefore recovery does slow down & therefore we advise you to decrease or stop smoking because it delay your recovery.')
        return []


class ActionAlcohol(Action):

    def name(self):
        return "action_alcohol"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'No, Alcohol will create more problem. It leads to decrement in Throat Immunity. Some people think that Alcohol based sanitizers are used for washing hands and it kills virus. So Alcohol Consumption will also kill it but it is wrong.')
        dispatcher.utter_message(
            'Because sanitizers is used on palm. Corona Virus affects only palm not cell but in body Corona  Virus is in Cells .More Alcohol can lead to drowsy & Vomitting starts. So it became dangerous specially effects lever & lungs.')
        return []


class ActionWhenTest(Action):

    def name(self):
        return "action_when_test"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'As Weather is changing so it may be symptoms of flu or cold or due to other circulating virus. If you have only cold & cough & Fever  than no need to test unless you meet two condition First one is have been in close contact with a person known to have CORONA VIRUS or have recently travelled from an area with Corona in last 14 days  or you come in close contact with infected person in last 14 days.')
        dispatcher.utter_message(
            'If you develop symptoms such as fever, cough, and/or difficulty breathing, and have been in close contact with a person known to have CORONA VIRUS or have recently travelled from an area with Corona or you come in close contact with infected person.')
        dispatcher.utter_message(
            'Stay home and call your healthcare provider. Older patients and individuals who have severe underlying medical conditions or are immune compromised should contact their healthcare provider early, even if their illness is mild.')
        return []


class ActionEmergencySymptoms(Action):

    def name(self):
        return "action_emergency_symptoms"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'If you have severe symptoms, such as persistent pain or pressure in the chest, new confusion or inability to arouse, or bluish lips of face, contact your healthcare provider or emergency room and seek care immediately.')
        return []


class ActionStigma(Action):

    def name(self):
        return "action_stigma"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'People can fight stigma and help, not hurt, others by providing social support. Counter stigma by learning and sharing facts. Communicating the facts that viruses do not target specific racial or ethnic groups, by caste, by religion  and how CORONA VIRUS actually spreads can help stop stigma.')
        return []


class ActionFuneral(Action):

    def name(self):
        return "action_funeral"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'There is currently no known risk associated with being in the same room at a funeral or visitation service with the body of someone who died of CORONA VIRUS.')
        return []


class ActionDeadbody(Action):

    def name(self):
        return "action_deadbody"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'CORONA VIRUS is a new disease and we are still learning how it spreads. The virus that causes CORONA VIRUS is thought to mainly spread from close contact (i.e., within about 6 feet) with a person who is currently sick with CORONA VIRUS. People should consider not touching the body of someone who has died of CORONA VIRUS.')
        dispatcher.utter_message(
            'Older people and people of all ages with severe underlying health conditions are at higher risk of developing serious CORONA VIRUS illness. There may be less of a chance of the virus spreading from certain types of touching, such as holding the hand or hugging after the body has been prepared for viewing. Other activities, such as kissing, washing, and shrouding should be avoided before, during, and after the body has been prepared, if possible.')
        dispatcher.utter_message(
            'If washing the body or shrouding are important religious or cultural practices, families are encouraged to work with their community cultural and religious leaders and funeral home staff on how to reduce their exposure as much as possible. At a minimum, people conducting these activities should wear disposable gloves.')
        return []


class ActionPets(Action):

    def name(self):
        return "action_pets"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'While this virus seems to have emerged from an animal source, it is now spreading from person-to-person in China. There is no reason to think that any animals including pets in the India  might be a source of infection with this new coronavirus.')
        dispatcher.utter_message(
            'To date, CDC has not received any reports of pets or other animals becoming sick with CORONA VIRUS. At this time, there is no evidence that companion animals including pets can spread CORONA VIRUS. However, since animals can spread other diseases to people, it’s always a good idea to wash your hands after being around animals.')
        return []


class ActionInfectedPets(Action):

    def name(self):
        return "action_infected_pets"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'You should restrict contact with pets and other animals while you are sick with CORONA VIRUS, just like you would around other people. Although there have not been reports of pets or other animals becoming sick with CORONA VIRUS, it is still recommended that people sick with CORONA VIRUS limit contact with animals until more information is known about the virus.')
        return []


class ActionEatNonveg(Action):

    def name(self):
        return "action_eat_nonveg"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Again data is not available. But  you can eat . This migrated from animal but now it is human virus so no data is available that is spread through animal now. So You can eat well cooked food . In China people eat animals  without cook so it transfer to human . But if you eat cooked non vegetarian than there is no danger.')
        return []


class ActionLightly(Action):

    def name(self):
        return "action_lighltly"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Actually this virus spread from those persons who travelled foreign countries where Corona Virus have outbreak & someone comes in close contact with those persons.')
        return []


class ActionDrinkWater(Action):

    def name(self):
        return "action_drink_water"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'No it is not true. But drinking water increase hydration & you feel well. Immunity work well.')
        return []


class ActionCurrency(Action):

    def name(self):
        return "action_currency"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Not only currency note but also other material for transaction that pass from many hands like Credit Cards than it can lead to spread of Corona on Hands . So wash hands properly.')
        return []


class ActionBreatMilk(Action):

    def name(self):
        return "action_breat_milk"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'In limited studies on women with COVID-19 and another coronavirus infection, Severe Acute Respiratory Syndrome (SARS-CoV), the virus has not been detected in breast milk; however we do not know whether mothers with COVID-19 can transmit the virus via breast milk.')
        dispatcher.utter_message(
            'A mother with confirmed CORONA VIRUS or who is a symptomatic PUI should take all possible precautions to avoid spreading the virus to her infant, including washing her hands before touching the infant and wearing a face mask, if possible, while feeding at the breast.')
        dispatcher.utter_message(
            'If expressing breast milk with a manual or electric breast pump, the mother should wash her hands before touching any pump or bottle parts and follow recommendations for proper pump cleaning after each use.')
        return []


class ActionProtectChildren(Action):

    def name(self):
        return "action_protect children"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'You can encourage your child to help stop the spread of COVID-19 by teaching them to do the same things everyone should do to stay healthy.')
        dispatcher.utter_message('Clean hands often using soap and water or alcohol-based hand sanitizer.')
        dispatcher.utter_message('Avoid people who are sick (coughing and sneezing).')
        dispatcher.utter_message(
            'Clean and disinfect high-touch surfaces daily in household common areas (e.g. tables, hard-backed chairs, doorknobs, light switches, remotes, handles, desks, toilets, sinks')
        dispatcher.utter_message(
            '•	Launder items including washable plush toys as appropriate in accordance with the manufacturer’s instructions. If possible, launder items using the warmest appropriate water setting for the items and dry items completely. Dirty laundry from an ill person can be washed with other people’s items.')
        return []


class ActionSymptomsChildren(Action):

    def name(self):
        return "action_symptoms_children"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'The symptoms of COVID-19 are similar in children and adults. However, children with confirmed COVID-19 have generally presented with mild symptoms.')
        dispatcher.utter_message(
            'Reported symptoms in children include cold-like symptoms, such as fever, runny nose, and cough. Vomiting and diarrhea have also been reported.')
        return []


class ActionSchoolDismissal(Action):

    def name(self):
        return "action_school_dismissal"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Limit Social Interactions: The key to slowing the spread of COVID-19 is to limit social interactions as much as possible. Parents should minimize play dates, and if held, parents should keep the groups small. Advise older children to hang out in a small group and to meet up outside rather than inside. It’s easier to keep and maintain space between others in outdoor settings, like parks.')
        dispatcher.utter_message(
            'Practice Social Distancing: If you have small meetups, consider hanging out with another family or friend who is also taking extra measures to put distance between themselves and others (i.e. social distancing).')
        dispatcher.utter_message(
            'Clean and Disinfect: Make sure children practice everyday preventive behaviors, such as cleaning and then disinfecting frequently touched surfaces.')
        dispatcher.utter_message(
            'Revise Spring Break & Travel Plans: Parents should help their older children revise spring break plans that included non-essential travel to crowded areas.')
        dispatcher.utter_message(
            'Remember, if children meet outside of school in bigger groups, it can put everyone at risk.')
        return []


class ActionStudyLoss(Action):

    def name(self):
        return "action_study_loss"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Help children continue learning.')
        dispatcher.utter_message(
            'Many schools are adapting in-person lessons to online or virtual learning. Review assignments from the school, and help your child establish a reasonable pace for completing the work.')
        dispatcher.utter_message(
            'You may need to assist your child with turning on devices, reading instructions, and typing Answer')
        return []


class ActionWaterSpreading(Action):

    def name(self):
        return "action_water_spreading"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('COVID-19 virus has not been detected in drinking water.')
        dispatcher.utter_message(
            'Conventional water treatment methods that use filtration and disinfection, such as those in most municipal drinking water systems, should remove or inactivate the virus that causes COVID-19.')
        return []


class ActionPool(Action):

    def name(self):
        return "action_pool"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'There is no evidence that COVID-19 can be spread to humans through the use of pools and hot tubs.')
        dispatcher.utter_message(
            'Proper operation, maintenance, and disinfection (e.g., with chlorine and bromine) of pools and hot tubs should remove or inactivate the virus that causes COVID-19.')
        return []


class ActionSewarage(Action):

    def name(self):
        return "action_sewarage"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'All data on COVID-19 transmission as information becomes available. At this time, the risk of transmission of the virus that causes COVID-19 through sewerage systems is thought to be low.')
        dispatcher.utter_message(
            'Although transmission of COVID-19 through sewage may be possible, there is no evidence to date that this has occurred. This guidance will be updated as necessary as new evidence is assessed.')
        return []


class ActionHiv(Action):

    def name(self):
        return "action_hiv"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'At the present time, we have no specific information about the risk of COVID-19 in people with HIV.')
        dispatcher.utter_message(
            'The risk from immune suppression is not known, but with other viral respiratory infections, the risk for people with HIV getting very sick is greatest in')
        dispatcher.utter_message(
            'People with a low CD4 cell count, and People not on HIV treatment (antiretroviral therapy or ART).')
        dispatcher.utter_message(
            'People with HIV can also be at increased risk of getting very sick with COVID-19 based on their age and other medical conditions.')
        return []


class ActionHivMedicine(Action):

    def name(self):
        return "action_hiv_medicine"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Some types of HIV medicine (in particular, lopinavir/ritonavir) are being evaluated in clinical trialsexternal icon to treat COVID-19.')
        dispatcher.utter_message(
            'While there is some evidence that this type of HIV medicine might help treat infections with SARS and MERS (two other coronaviruses related to the virus that causes COVID-19), there are no data available yet from clinical trials that these drugs help people with COVID-19.')
        dispatcher.utter_message(
            'People with HIV should not switch their HIV medicine in an attempt to prevent or treat COVID-19.')
        return []


class ActionAsthama(Action):

    def name(self):
        return "action_asthama"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'People with asthma may be at higher risk of getting very sick from COVID-19.  COVID-19 can affect your respiratory tract (nose, throat, lungs), cause an asthma attack, and possibly lead to pneumonia and acute respiratory disease.')
        return []


class ActionOrigin(Action):

    def name(self):
        return "action_origin"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Corona Virus origin from animal that is bat in  China. It originated from China in December-2019.W.H.O called it Novel Covid-19 because it belongs from Covid Family.Many people get infected due to human to human spreading  property.People were not aware about it at that time.So they did mistakes.Meanwhile many people of different countries were unaware.Chinese visited other countries & people from different countries visited like Italy,Saudi Arabia,USA etc. So these country also get infected.Today mostly affected countries are China,Italy,USA,Spain,Germany,Iran,South Korea,UK,Norway,Switzerland,Canada,Pakistan etc. India is on 43rd Number.')
        return []


class ActionOrigin(Action):
    def name(self):
        return "action_origin"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Corona Virus origin from animal that is bat in  China. It originated from China in December-2019.W.H.O called it Novel Covid-19 because it belongs from Covid Family.Many people get infected due to human to human spreading  property.People were not aware about it at that time.So they did mistakes.Meanwhile many people of different countries were unaware.Chinese visited other countries & people from different countries visited like Italy,Saudi Arabia,USA etc. So these country also get infected.Today mostly affected countries are China,Italy,USA,Spain,Germany,Iran,South Korea,UK,Norway,Switzerland,Canada,Pakistan etc. India is on 43rd Number.')
        return []


class HowTest(Action):
    def name(self):
        return "action_how_test"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Test Process is that First Primary Test perform in which sample of mucus or cough taken from lungs or saliva,nose')
        return []


class TestCost(Action):
    def name(self):
        return "action_test_cost"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'The cost of Test in Private Lab is Rs. 4500 as Indian Govt.(ICMR) issues guidelines cost should not exceed   Rs 500. It includes Rs. 1500 for screening & Rs. 3000 for Confirmation Test. In Govt. Lab its free but they will perform test according to their strategy.')
        return []


class TestSelfGo(Action):
    def name(self):
        return "action_self_go"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'You cannot go to the Laboratory directly by your own. If you have symptoms or suspect  than Call Helpline Numbers than they will ask some questions. According to your answer if they think that you should tested than they will inform to nearest Lab & send PCR Van.So Samples are collected at Home')
        return []


class TestProcess(Action):
    def name(self):
        return "action_test_process"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'PCR Van will collect samples of mucus of Nose,Throat,Lungs, Saliva from Home & sent Labaroatory. It is tested . This is called Primary Test or Scrrening. If Corona Test is Positive than for reconfirmation it again tested. This is called Secondary or Confirmation test.Primary test take 1-2 Hours & Secondary Test take 3-4 Hours. Sometime Secondary Test facility is not available in Some Labs than Sample sent to NIV Laboratory')
        return []


class TestStrategy(Action):
    def name(self):
        return "action_test_strategy"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            'Government define that test will performed on priority base that is if you meet some criteria like 1.  All asymptomatic individuals who have undertaken international travel in the last 14 days.All symptomatic contacts of laboratory confirmed cases.All symptomatic health care workers.')
        dispatcher.utter_message(
            'All hospitalized patients with Severe Acute Respiratory Illness (fever AND cough and/orshortness of breath).Asymptomatic direct and high-risk contacts of a confirmed case should be tested once between day 5 and day 14 of coming in his/her contact.')
        return []
