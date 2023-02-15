import xml.etree.ElementTree as ET

def crear_xml_estudiantes():

    # Crear el elemento raíz 'students'
    root = ET.Element('students')

    # Crear cinco elementos hijos 'student' y añadirlos al elemento raíz
    student1 = ET.SubElement(root, 'student')
    ET.SubElement(student1, 'name').text = "Gisela"
    ET.SubElement(student1, 'surname').text = "Fernandez"
    ET.SubElement(student1, 'email').text = "ernail@gmail.com"
    ET.SubElement(student1, 'dni').text = "436573575X"

    student2 = ET.SubElement(root, 'student')
    ET.SubElement(student2, 'name').text = "Blanca"
    ET.SubElement(student2, 'surname').text = "Velasco"
    ET.SubElement(student2, 'email').text = "remaol@gmail.com"
    ET.SubElement(student2, 'dni').text = "2532562642J"

    student3 = ET.SubElement(root, 'student')
    ET.SubElement(student3, 'name').text = "Irina"
    ET.SubElement(student3, 'surname').text = "Raval"
    ET.SubElement(student3, 'email').text = "glimail@gmail.com"
    ET.SubElement(student3, 'dni').text = "246373735D"

    student4 = ET.SubElement(root, 'student')
    ET.SubElement(student4, 'name').text = "Alba"
    ET.SubElement(student4, 'surname').text = "Alonso"
    ET.SubElement(student4, 'email').text = "mlimail@gmail.com"
    ET.SubElement(student4, 'dni').text = "57685859799Z"

    student5 = ET.SubElement(root, 'student')
    ET.SubElement(student5, 'name').text = "Alex"
    ET.SubElement(student5, 'surname').text = "Gutierrez"
    ET.SubElement(student5, 'email').text = "klamail@gmail.com"
    ET.SubElement(student5, 'dni').text = "6595796976S"

    ET.indent(root)

    tree = ET.ElementTree(root)
    tree.write('estudiantes.xml')

    # Muestra el XML por consola
    ET.dump(root)

crear_xml_estudiantes()
