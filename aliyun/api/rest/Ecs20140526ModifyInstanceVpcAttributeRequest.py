'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Ecs20140526ModifyInstanceVpcAttributeRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.InstanceId = None
		self.PrivateIpAddress = None
		self.VSwitchId = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.ModifyInstanceVpcAttribute.2014-05-26'
