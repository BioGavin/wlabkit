#!/usr/bin/python3
# description: extract isolation-source information for each biosample from xml file and output a tsv file
# usage: python3 parse_biosample_xml.py biosample_demo.xml

import xml.sax
import pandas as pd
import sys


class BioSampleHandler(xml.sax.ContentHandler):
   def __init__(self):
      self.CurrentTag = ""
      self.CurrentAttributes = {}
      self.CurrentID = ""
      self.accession = ""
      self.accessions = []
      self.isolation_source = ""
      self.isolation_sources = []
      self.counter = 0

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentTag = tag
      self.CurrentAttributes = attributes
      if tag == "BioSample":
         try:
            self.accession = attributes["accession"]
            # print ("Accession:", self.accession)
         except:
            pass


   # Call when an elements ends
   def endElement(self, tag):
      if tag == "BioSample":
         self.accessions.append(self.accession)
         self.isolation_sources.append(self.isolation_source)
         print(f'{self.counter} + {self.accession}')
         self.isolation_source = ''
         self.accession = ''
         self.counter += 1
         
      
   # Call when a character is read
   def characters(self, content):
      """extract isolation-source information for each biosample"""
      if self.CurrentTag == "Attribute" and self.CurrentAttributes["attribute_name"] == "isolation-source":
         # print(content)
         if content.strip():
            self.isolation_source = content
      if self.CurrentTag == "Attribute" and self.CurrentAttributes["attribute_name"] == "isolation_source":
         # print(content)
         if content.strip():
            self.isolation_source = content
      if self.CurrentTag == "Attribute" and self.CurrentAttributes["attribute_name"] == "isolation source":
         # print(content)
         if content.strip():
            self.isolation_source = content

      

if ( __name__ == "__main__"):

   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = BioSampleHandler()
   parser.setContentHandler(Handler)

   parser.parse(sys.argv[1])

   accession_dat = Handler.accessions
   isolation_source_dat = Handler.isolation_sources
   # print(accession_dat, isolation_source_dat)
   
   df = pd.DataFrame({
      "biosample": accession_dat,
      "isolation_source": isolation_source_dat
   })
   df.drop(df[df.biosample==''].index,inplace=True)
   
   df.to_csv('biosample_isolation_source.tsv', sep='\t', index=False)

