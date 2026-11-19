# Transport Protocol - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Transport Protocol**

## CodeSystem: Transport Protocol 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/transport-protocol | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:TransportProtocolCS |

 
The transport protocol or mechanism used to carry the exchange. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Transport Protocol](ValueSet-transport-protocol.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "transport-protocol",
  "url" : "http://smart.who.int/base/CodeSystem/transport-protocol",
  "version" : "0.3.0",
  "name" : "TransportProtocolCS",
  "title" : "Transport Protocol",
  "status" : "draft",
  "date" : "2026-09-07T06:11:01+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "The transport protocol or mechanism used to carry the exchange.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 10,
  "concept" : [{
    "code" : "http",
    "display" : "HTTP/REST",
    "definition" : "Exchange over HTTP or HTTPS using RESTful conventions."
  },
  {
    "code" : "soap",
    "display" : "SOAP",
    "definition" : "Exchange using SOAP web services."
  },
  {
    "code" : "mllp",
    "display" : "MLLP",
    "definition" : "Minimal Lower Layer Protocol, used for HL7 v2 messaging."
  },
  {
    "code" : "smtp",
    "display" : "SMTP",
    "definition" : "Exchange via email (e.g., Direct messaging)."
  },
  {
    "code" : "ftp",
    "display" : "FTP/SFTP",
    "definition" : "File-based exchange via FTP or SFTP."
  },
  {
    "code" : "dicom",
    "display" : "DICOM",
    "definition" : "DICOM network protocol for imaging exchange."
  },
  {
    "code" : "websocket",
    "display" : "WebSocket",
    "definition" : "Persistent bidirectional connection."
  },
  {
    "code" : "amqp",
    "display" : "AMQP",
    "definition" : "Advanced Message Queuing Protocol."
  },
  {
    "code" : "kafka",
    "display" : "Kafka",
    "definition" : "Event streaming via Apache Kafka or similar platforms."
  },
  {
    "code" : "filesystem",
    "display" : "File System",
    "definition" : "Exchange via shared file system or media."
  }]
}

```
