import shutil, logging, json, time, sys, traceback

from modules.Configuration import Configuration
from modules.BaseContainer import BaseContainer
from modules.PcapProcessor import PcapProcessor

logger = logging.getLogger(__name__)

class CaptureContainer(BaseContainer):
	
	def __init__(self):
		BaseContainer.__init__(self, Configuration().get("dockerDaemonHostUrl"), Configuration().get("captureContainerName"))

	def deployContainer(self):
		try:
			logger.debug("Deploying new Capture container [%s]" % Configuration().get("captureContainerName"))
			container = self.cli.containers.run(	image=Configuration().get("captureContainerImage"),
														name=Configuration().get("captureContainerName"), 
														restart_policy={"Name": "on-failure"},
														volumes={Configuration().get("dataDirectory") + '/capture': {'bind': Configuration().get("dataDirectory") + '/capture', 'mode': 'rw'}},
														#network_mode="host",
														network_mode="container:" + Configuration().get("victimContainerName"),
														#network="whaler_default",
														detach=True,
														command='-U -W 1 -C 50 -w ' + Configuration().get("dataDirectory") + '/capture/capfile -i eth0',
														
			)
			
			self.container=container
			logger.info("deployed new container [%s]" % container.name)
			

		except Exception as e:
			logger.error("failed deploying new container [%s]" %e)

	def getPcapFileReport(self, containerName):
		report = PcapProcessor(containerName, Configuration().get("dataDirectory") + "/capture/capfile").getSummaryReport()
		# strReport = json.dumps(report, sort_keys=True,indent=4)
		# logging.debug(strReport)
		return report

	def archiveCaptureFile(self, container, pCapFileStoragePath):
		try:
			shutil.copyfile(Configuration().get("dataDirectory") + "/capture/capfile", pCapFileStoragePath + "/capture.pcap")
			logger.info(">>Saved Pcap file(s) to %s/capture.pcap" % pCapFileStoragePath)
			
		except Exception as e:
			logger.error("Error archiving capture file [%s]" % e)
			traceback.print_exc(file=sys.stdout)


