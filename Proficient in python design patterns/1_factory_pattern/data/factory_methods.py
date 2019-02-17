#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import json


class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = ET.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    try:
        con = connector(filepath)
    except Exception as e:
        print(str(e))
        return
    # return connector(filepath)
    return con


def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


def main():
    sqlite_factory = connect_to('data/person.sq3')
    print()
    filepath = r'C:\Users\liming\Desktop\data\person.xml'
    xml_factory = connect_to(filepath)
    # print(xml_factory)
    if xml_factory != None:

        xml_data = xml_factory.parsed_data
        # print(xml_data)
        liars = xml_data.findall(".//{}[{}='{}']".format('person',
                                                         'lastName', 'Liar'))
        print('found: {} persons'.format(len(liars)))
        for liar in liars:
            print('first name: {}'.format(liar.find('firstName').text))
            print('last name: {}'.format(liar.find('lastName').text))
            [print('phone number ({})'.format(p.attrib['type']),
                   p.text) for p in liar.find('phoneNumbers')]
    print()
    filepath = r'C:\Users\liming\Desktop\data\donut.json'
    json_factory = connect_to(filepath)
    json_data = json_factory.parsed_data
    print(json_data)
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        [print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]


if __name__ == '__main__':
    main()
