from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, AllSlotsReset
import io




class ActionInfraCost(Action):
	def name(self):
		return 'action_infra_cost'
		
	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "300k is the infra YTD(till April 2019)"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]


class ActionPeoplesCost(Action):
	def name(self):
		return 'action_peoples_cost'
	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "400k is the people YTD(till April 2019)"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionBothCosts(Action):
	def name(self):
		return 'action_both_costs'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = '''300k is the infra YTD(till April 2019)
			\n400k is the people YTD(till April 2019) '''
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionTechnologies(Action):
	def name(self):
		return 'action_technologies'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = '''1.Oracle
	    \n2.Weblogic
	    \n3.Redhat linux
	    \n4.Windows
	    \n5.HP Storage
	    \n6.Message Broker'''
		dispatcher.utter_message("These are the technologies which are currently using:")

		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class Actionjanuarypeoplescost(Action):
	def name(self):
		return 'action_january_peoples_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "1000 is the peoples cost."
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class Actionfebruaryfebpeoplescost(Action):
	def name(self):
		return 'action_Februaryfeb_peoples_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "1220 is the peoples cost."
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class Actionmarchpeoplescost(Action):
	def name(self):
		return 'action_March_peoples_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "1440 is the peoples cost."
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class Actionaprilpeoplescost(Action):
	def name(self):
		return 'action_april_peoples_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "1660 is the peoples cost."
		dispatcher.utter_message(response)
		return [AllSlotsReset()]


class Actionmaypeoplescost(Action):
	def name(self):
		return 'action_may_peoples_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "1880 is the peoples cost."
		dispatcher.utter_message(response)
		return [AllSlotsReset()]



class Actionjunpeoplescost(Action):
	def name(self):
		return 'action_jun_peoples_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "2100 is the peoples cost."
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class Actionjulypeoplescost(Action):
	def name(self):
		return 'action_July_peoples_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "2320 is the peoples cost."
		dispatcher.utter_message(response)
		return [AllSlotsReset()]


class Actionaugustpeoplescost(Action):
	def name(self):
		return 'action_august_peoples_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "2540 is the peoples cost."
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class Actionseppeoplescost(Action):
	def name(self):
		return 'action_sep_peoples_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "2760 is the peoples cost."
		dispatcher.utter_message(response)
		return [AllSlotsReset()]


class Actionoctpeoplescost(Action):
	def name(self):
		return 'action_oct_peoples_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "2980 is the peoples cost."
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class Actionnovpeoplescost(Action):
	def name(self):
		return 'action_nov_peoples_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "3200 is the peoples cost."
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class Actiondecpeoplescost(Action):
	def name(self):
		return 'action_Dec_peoples_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "3420 is the peoples cost."
		dispatcher.utter_message(response)
		return [AllSlotsReset()]


class Actionjaninfracost(Action):
	def name(self):
		return 'action_jan_infra_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "120302 is the infra cost in January 2019"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]


class Actionfebinfracost(Action):
	def name(self):
		return 'action_feb_infra_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "120504 is the infra cost in February 2019"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]


class Actionmarinfracost(Action):
	def name(self):
		return 'action_Mar_infra_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "120334 is the infra cost in March 2019"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]


class Actionaprilinfracost(Action):
	def name(self):
		return 'action_april_infra_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "122504 is the infra cost in April 2019"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class Actionmayinfracost(Action):
	def name(self):
		return 'action_May_infra_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "120345 is the infra cost in May 2019"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class Actionjuneinfracost(Action):
	def name(self):
		return 'action_June_infra_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "123503 is the infra cost in June 2019"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class Actionjulyinfracost(Action):
	def name(self):
		return 'action_July_infra_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "120302 is the infra cost in July 2019"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class Actionaugustinfracost(Action):
	def name(self):
		return 'action_august_infra_cost'




	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "120313 is the infra cost in August 2019"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class Actionsepinfracost(Action):
	def name(self):
		return 'action_sep_infra_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "120433 is the infra cost in September 2019"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class Actionoctinfracost(Action):
	def name(self):
		return 'action_oct_infra_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "120557 is the infra cost in October 2019"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]


class Actionnovinfracost(Action):
	def name(self):
		return 'action_nov_infra_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "120313 is the infra cost in November 2019"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class Actiondecinfracost(Action):
	def name(self):
		return 'action_dec_infra_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "120433 is the infra cost in December 2019"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionVersion(Action):
	def name(self):
		return 'action_version'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "Currently you are using Oracle 11.0.01 and Oracle 12.1 in Production"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]



class ActionNoOfDbs(Action):
	def name(self):
		return 'action_no_of_dbs'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "5 databases with 20 schemas"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionCriticality(Action):
	def name(self):
		return 'action_criticality'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "High"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class ActionAccessManagement(Action):
	def name(self):
		return 'action_access_management'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "Business user access is done via BURA"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class Actionno_of_apps(Action):
	def name(self):
		return 'action_no_of_apps'

	def run(self, dispatcher, tracker, domain):
		response = "21 applications  are currently using BURA for access management "
		dispatcher.utter_message(response)
		return []


class ActionnoReleases(Action):
	def name(self):
		return 'action_releases'

	def run(self, dispatcher, tracker, domain):
		app1 = tracker.get_slot('app1')
		app2 = tracker.get_slot('app2')
		response = '''{}:10 Releases
		\n {}: 5 releases'''.format(app1,app2)
		dispatcher.utter_message(response)
		return []

class ActionDeploy(Action):
	def name(self):
		return 'action_deploy'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app is deployed in Asia"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]


class ActionAppOwner(Action):
	def name(self):
		return 'action_app_owner'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The owner of the app is john"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]


class ActionAppProductGroup(Action):
	def name(self):
		return 'action_app_product_group'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "database mgmt,OS,Hardware,messaging,application server,log,Integration,Business intelligence"
		dispatcher.utter_message("These are the product groups maintained by the app:")
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class ActionAppProducts(Action):
	def name(self):
		return 'action_app_products'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "oracle,sybase,Linux,Linux,HP,IBM,Java,splunk"
		dispatcher.utter_message("These are the app products")
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class ActionAppReleaseDate(Action):
	def name(self):
		return 'action_app_release_date'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app release date is 25-1-2019"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class ActionAppImpactedRegions(Action):
	def name(self):
		return 'action_app_impacted_regions'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "tokyo, singapore,mumbai, hongkong,thailand,pune"
		dispatcher.utter_message("These are the app impacted regions:")
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppProvider(Action):
	def name(self):
		return 'action_app_provider'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app provider is robert"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class ActionAppSponsor(Action):
	def name(self):
		return 'action_app_sponsor'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app sponsor is Sarah"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppEndDate(Action):
	def name(self):
		return 'action_app_end_date'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app end date is Jul-25"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppProviderOrganization(Action):
	def name(self):
		return 'action_app_Provider_organization'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The provider organisations of the app are Finance  and IT"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppSponsorOrganization(Action):
	def name(self):
		return 'action_app_sponsor_organization'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app sponsor organisation is Finance"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppId(Action):
	def name(self):
		return 'action_app_app_id'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app id is APP-123"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppAssessmentDate(Action):
	def name(self):
		return 'action_app_assessment_date'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app assessment date is 1-1-2019"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppOwnerStatus(Action):
	def name(self):
		return 'action_app_owner_status'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app owner status is Complete"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppOwmerSignoffDate(Action):
	def name(self):
		return 'action_owmer_signoff_date'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app owner signoff status is 4-2-2019"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppProviderSignoffDate(Action):
	def name(self):
		return 'action_provider_signoff_date'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app provider signoff date is 17-1-2019"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppSponsorSignoffDate(Action):
	def name(self):
		return 'action_sponsor_signoff_date'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app sponsor signoff date is 10-2-2019"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]



class ActionYearOfAssessment(Action):
	def name(self):
		return 'action_year_of_assessment'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The year of assessment is 2018"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]


class ActionAppNoOfServers(Action):
	def name(self):
		return 'action_app_no_of_servers'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "You have currently 4 oracle 11g servers"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]



class ActionAppServerName(Action):
	def name(self):
		return 'action_app_server_name'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "Server_122,Server_110,Server_115,Server_125"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionEndOfVersion(Action):
	def name(self):
		return 'action_end_of_version'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The end of version date is 1-1-2020"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionProductCost(Action):
	def name(self):
		return 'action_product_cost'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app product cost is 2600"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]


class ActionAppVolumes(Action):
	def name(self):
		return 'action_app_volumes'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "volumes are 109"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionReminderSchedule(Action):
	def name(self):
		return 'action_reminder_schedule'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "vikram"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionReleaseType(Action):
	def name(self):
		return 'action_release_type'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The release type is Major"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppEmployeePlaceName(Action):
	def name(self):
		return 'action_app_employee_place_name'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response ='''Rochester
		\nMesa
		\nAtlanta
		\nReddick'''
		dispatcher.utter_message("This is the list of employee place name")
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]



class ActionAppEmployeeId(Action):
	def name(self):
		return 'action_app_employee_id'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = '''5424563
		\n5453345
		\n6547744
		\n6767851'''
		dispatcher.utter_message("This is the list of employee id")
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppEmployeeFirstName(Action):
	def name(self):
		return 'action_app_employee_first_name'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response ='''Jeni
		\nAngelique
		\nDonald
		\nSteven'''
		dispatcher.utter_message("This is the list of employee first name")
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]



class ActionAppmEployeeLastName(Action):
	def name(self):
		return 'action_app_employee_last_name'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = '''Shaffer
		\nGoodwin
		\nFarris
		\nRendon'''
		dispatcher.utter_message("This is the list of employee last name")

		dispatcher.utter_message(response)
		return [SlotSet("app", app)]


class ActionAppEmployeeEmail(Action):
	def name(self):
		return 'action_app_employee_email'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = '''jeni.shaffer@HILA.com
		\ndonald.farris@bellsouth.net
		\nsteven.rendon@HILA.com
		\nalmeta.brookins@HILA.com'''
		dispatcher.utter_message("This is the list of employee email id")
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]


class ActionAppEmployeeCountry(Action):
	def name(self):
		return 'action_app_employee_country'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = '''Monroe
		\nCrenshaw
		\nFranklin
		\nChampaign'''
		dispatcher.utter_message("This is the list of employee country")
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppEmployeeCity(Action):
	def name(self):
		return 'action_app_employee_city'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = '''Rochester
		\nLuverne
		\nHodges
		\nSavoy'''
		dispatcher.utter_message("This is the list of employee city")
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppEmployeeState(Action):
	def name(self):
		return 'action_app_employee_state'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = '''NY
		\nAL
		\nIL
		\nMO'''
		dispatcher.utter_message("This is the list of employee state")
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppEmployeeRegion(Action):
	def name(self):
		return 'action_app_employee_region'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = '''Northeast
		\nSouth
		\nMidwest
		\nNorthEast'''
		dispatcher.utter_message(response)
		dispatcher.utter_message("This is the list of employee region")
		return [SlotSet("app", app)]

class ActionProviderSignoff(Action):
	def name(self):
		return 'action_app_provider_signoff'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app provider sign off state is Pending"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppAseessmentStatus(Action):
	def name(self):
		return 'action_app_aseessment_status'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app assessment status is Not started"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class ActionAppSponsorSignoff(Action):
	def name(self):
		return 'action_app_sponsor_signoff'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app sponsor signoff status is Complete"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class ActionAppBasel1Regulatory(Action):
	def name(self):
		return 'action_app_basel1_regulatory'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "No"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class ActionAppBasel2Regulatory(Action):
	def name(self):
		return 'action_app_Basel2_regulatory'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "Yes"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]

class ActionAppBasel3Regulatory(Action):
	def name(self):
		return 'action_app_Basel3_regulatory'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "No"
		dispatcher.utter_message(response)
		return [AllSlotsReset()]




class ActionAppAPACRegulatory(Action):
	def name(self):
		return 'action_app_APAC_regulatory'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "Yes"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]


class ActionAppBusinessCriticality(Action):
	def name(self):
		return 'action_app_Business_criticality'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = " The app business criticality is High"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]


class Actiongoodmorning(Action):
	def name(self):
		return 'action_good_morning'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "very good morning, How can I help you?"
		dispatcher.utter_message(response)
		dispatcher.utter_message("You can ask me questions related to infrastructure details")
		dispatcher.utter_message("Here are some Examples:")
		dispatcher.utter_message("How many applications are currently running  on BURA platform?")
		dispatcher.utter_message("Who is the owner of OPM?")
		return [SlotSet("app", app)]

class Actiongoodafternoon(Action):
	def name(self):
		return 'action_good_afternoon'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "very good afternoon, How can I help you?"
		dispatcher.utter_message(response)
		dispatcher.utter_message("You can ask me questions related to infrastructure details")
		dispatcher.utter_message("Here are some Examples:")
		dispatcher.utter_message("How many applications are currently running on BURA platform?")
		dispatcher.utter_message("Who is the owner of OPM?")
		return [SlotSet("app", app)]

class Actiongoodevening(Action):
	def name(self):
		return 'action_good_evening'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "very good evening, How can I help you?"
		dispatcher.utter_message(response)
		dispatcher.utter_message("You can ask me questions related to infrastructure details")
		dispatcher.utter_message("Here are some Examples:")
		dispatcher.utter_message("How many applications are currently running on BURA platform?")
		dispatcher.utter_message("Who is the owner of OPM?")
		return [SlotSet("app", app)]



class Actionhelp(Action):
	def name(self):
		return 'action_help'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "You can ask me questions related to infrastructure details "
		dispatcher.utter_message(response)
		dispatcher.utter_message("Here are some Examples:")
		dispatcher.utter_message("How many applications are currently running on BURA platform?")
		dispatcher.utter_message("Who is the owner of OPM?")
		return [SlotSet("app", app)]

class Actionname(Action):
	def name(self):
		return 'action_name'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "I am infra bot, I am here to explain the details of infrastructure. "
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class Actionhowareyou(Action):
	def name(self):
		return 'action_how_are_you'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "yeah good, How about you? "
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class Actionbotage(Action):
	def name(self):
		return 'action_bot_age'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "I was created just a few days ago"
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]

class Actionbotdetails(Action):
	def name(self):
		return 'action_bot_details'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "I am Infra bot, I am here to explain the details of infrastructure. "
		dispatcher.utter_message(response)
		dispatcher.utter_message("Here are some Examples:")
		dispatcher.utter_message("How many applications are currently running  on BURA platform?")
		dispatcher.utter_message("Who is the owner of OPM?")
		return [SlotSet("app", app)]

class Actionok(Action):
	def name(self):
		return 'action_ok'

	def run(self, dispatcher, tracker, domain):
		app = tracker.get_slot('app')
		response = "Do you want to ask me anything else? "
		dispatcher.utter_message(response)
		return [SlotSet("app", app)]