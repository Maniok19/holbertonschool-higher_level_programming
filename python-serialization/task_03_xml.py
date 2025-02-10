#!/usr/bin/python3
""" Module that contains a function that serializes a dictionary to XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a dictionary to XML"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserializes a dictionary from XML"""
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
