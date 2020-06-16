from ncclient import manager
import xml.dom.minidom

####################################################################################################
#                                                                                                   #
#               device is a type nclient.manager.Manager that can  manage                           #
#               all the rpc statement as a file                                                     #
#                                                                                                   #
#####################################################################################################


device = manager.connect(host="ios-xe-mgmt.cisco.com", port=10000, username="developer", password="C1sco12345", hostkey_verify=False, 
                         device_params={'name': 'default'}, allow_agent=False, look_for_keys=False)


hostname="""
  <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>test_netconf</hostname>
      </native>
    </config>
"""

bgp_RID="""
    <config>
      <bgp xmlns="http://openconfig.net/yang/bgp">
        <global>
          <config>
            <as>150</as>
            <router-id>125.121.140.24</router-id>
          </config>
        </global>
      </bgp>
    </config>
"""

username="""
 <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <username>
        <name>carlovalle</name>
        <privilege>15</privilege>
        <password>
          <password>cisco</password>
        </password>
      </username>
    </native>
  </config>
"""

edit_int_ieft="""
<config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                        <name>Loopback1</name>
                        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                        <enabled>true</enabled>
                        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                                <address>
                                        <ip>1.1.1.1</ip>
                                        <netmask>255.255.255.255</netmask>
                                </address>
                        </ipv4>
                </interface>
        </interfaces>
</config>
"""


#####################################################################################################
#                                                                                                   #
#               The method edit_config sends as parameters the xml format                           #
#               configuration based on yang openconfig and ietf data model
#               only have to change the first parameter in method edit_config                       #
#                                                                                                   #
#####################################################################################################


with device as m:
   edit = (m.edit_config(edit_int_ieft,target="running"))
print(edit)
