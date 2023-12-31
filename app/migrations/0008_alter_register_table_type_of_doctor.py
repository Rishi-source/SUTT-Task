# Generated by Django 4.2 on 2023-06-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_register_table_type_of_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_table',
            name='Type_of_Doctor',
            field=models.CharField(blank=True, choices=[('Cardiologist', 'Cardiologist'), ('Dermatologist', 'Dermatologist'), ('Endocrinologist', 'Endocrinologist'), ('Gastroenterologist', 'Gastroenterologist'), ('Neurologist', 'Neurologist'), ('Oncologist', 'Oncologist'), ('Pediatrician', 'Pediatrician'), ('Psychiatrist', 'Psychiatrist'), ('Radiologist', 'Radiologist'), ('Surgeon', 'Surgeon'), ('Orthopedic Surgeon', 'Orthopedic Surgeon'), ('Ophthalmologist', 'Ophthalmologist'), ('ENT Specialist', 'ENT Specialist'), ('Urologist', 'Urologist'), ('Nephrologist', 'Nephrologist'), ('Pulmonologist', 'Pulmonologist'), ('Allergist/Immunologist', 'Allergist/Immunologist'), ('Rheumatologist', 'Rheumatologist'), ('Hematologist', 'Hematologist'), ('Osteopath', 'Osteopath'), ('Chiropractor', 'Chiropractor'), ('Homeopath', 'Homeopath'), ('Ayurvedic Doctor', 'Ayurvedic Doctor'), ('Naturopath', 'Naturopath'), ('Physiotherapist', 'Physiotherapist'), ('Dentist', 'Dentist'), ('Veterinarian', 'Veterinarian')], max_length=250, null=True),
        ),
    ]
