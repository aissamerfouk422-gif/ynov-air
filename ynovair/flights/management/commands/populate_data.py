from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from flights.models import Airport, Flight, Meal, Passenger, Booking
import random


class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating airports...')

        # Créer des aéroports
        airports_data = [
            {'code': 'CDG', 'name': 'Aéroport Charles de Gaulle', 'city': 'Paris', 'country': 'France'},
            {'code': 'LYS', 'name': 'Aéroport Lyon-Saint Exupéry', 'city': 'Lyon', 'country': 'France'},
            {'code': 'MRS', 'name': 'Aéroport Marseille Provence', 'city': 'Marseille', 'country': 'France'},
            {'code': 'TLS', 'name': 'Aéroport Toulouse-Blagnac', 'city': 'Toulouse', 'country': 'France'},
            {'code': 'NCE', 'name': 'Aéroport Nice Côte d\'Azur', 'city': 'Nice', 'country': 'France'},
            {'code': 'NTE', 'name': 'Aéroport Nantes Atlantique', 'city': 'Nantes', 'country': 'France'},
            {'code': 'BOD', 'name': 'Aéroport de Bordeaux-Mérignac', 'city': 'Bordeaux', 'country': 'France'},
            {'code': 'BCN', 'name': 'Aéroport de Barcelone', 'city': 'Barcelone', 'country': 'Espagne'},
            {'code': 'MAD', 'name': 'Aéroport Madrid-Barajas', 'city': 'Madrid', 'country': 'Espagne'},
            {'code': 'LHR', 'name': 'Aéroport de Londres Heathrow', 'city': 'Londres', 'country': 'Royaume-Uni'},
        ]

        airports = {}
        for airport_data in airports_data:
            airport, created = Airport.objects.get_or_create(**airport_data)
            airports[airport.code] = airport
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created airport: {airport}'))

        self.stdout.write('Creating meals...')

        meals_data = [
            {'code': 'STANDARD', 'name': 'Standard', 'description': 'Repas standard', 'price': 0},
            {'code': 'VEGETARIEN', 'name': 'Végétarien', 'description': 'Repas végétarien', 'price': 5},
            {'code': 'VEGAN', 'name': 'Vegan', 'description': 'Repas vegan', 'price': 5},
            {'code': 'SANS_GLUTEN', 'name': 'Sans gluten', 'description': 'Repas sans gluten', 'price': 7},
            {'code': 'ENFANT', 'name': 'Enfant', 'description': 'Menu enfant', 'price': 3},
        ]

        for data in meals_data:
            meal, created = Meal.objects.get_or_create(code=data['code'], defaults=data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created meal: {meal}'))

        # Créer 50 plats supplémentaires
        for i in range(1, 51):
            code = f"MEAL{i:03d}"
            defaults = {
                'name': f"Plat {i}",
                'description': f"Description du plat {i}",
                'price': random.choice([0, 3, 5, 7, 10]),
                'is_active': True,
            }
            meal, created = Meal.objects.get_or_create(code=code, defaults=defaults)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created meal: {meal}'))

        self.stdout.write('Creating flights...')

        # Créer des vols
        routes = [
            ('CDG', 'LYS'), ('LYS', 'CDG'),
            ('CDG', 'MRS'), ('MRS', 'CDG'),
            ('CDG', 'TLS'), ('TLS', 'CDG'),
            ('CDG', 'NCE'), ('NCE', 'CDG'),
            ('LYS', 'MRS'), ('MRS', 'LYS'),
            ('LYS', 'TLS'), ('TLS', 'LYS'),
            ('CDG', 'BCN'), ('BCN', 'CDG'),
            ('CDG', 'MAD'), ('MAD', 'CDG'),
            ('CDG', 'LHR'), ('LHR', 'CDG'),
            ('LYS', 'BCN'), ('BCN', 'LYS'),
        ]

        flight_number = 100
        for origin_code, dest_code in routes:
            origin = airports[origin_code]
            destination = airports[dest_code]

            # Créer plusieurs vols pour chaque route
            for day in range(7):
                for hour in [8, 12, 16, 20]:
                    departure_time = timezone.now() + timedelta(days=day, hours=hour)
                    duration = timedelta(hours=random.randint(1, 3), minutes=random.randint(0, 59))
                    arrival_time = departure_time + duration

                    total_seats = random.choice([150, 180, 200, 250])
                    available_seats = random.randint(int(total_seats * 0.3), total_seats)
                    price = random.randint(50, 300)

                    flight, created = Flight.objects.get_or_create(
                        flight_number=f'YN{flight_number}',
                        defaults={
                            'origin': origin,
                            'destination': destination,
                            'departure_time': departure_time,
                            'arrival_time': arrival_time,
                            'duration': duration,
                            'available_seats': available_seats,
                            'total_seats': total_seats,
                            'price': price,
                            'status': 'SCHEDULED'
                        }
                    )

                    if created:
                        self.stdout.write(f'Created flight: {flight}')

                    flight_number += 1

        self.stdout.write('Creating passengers...')

        first_names = [
            'Alex', 'Marie', 'Jean', 'Paul', 'Luc', 'Emma', 'Léa', 'Nina', 'Tom', 'Eva',
            'Noah', 'Liam', 'Mia', 'Zoe', 'Lola', 'Anna', 'Hugo', 'Leo', 'Ryan', 'Sara'
        ]
        last_names = [
            'Martin', 'Bernard', 'Thomas', 'Petit', 'Robert', 'Richard', 'Durand', 'Dubois', 'Moreau', 'Laurent',
            'Simon', 'Michel', 'Lefebvre', 'Leroy', 'Roux', 'David', 'Bertrand', 'Morel', 'Fournier', 'Girard'
        ]

        passengers = []
        from datetime import date
        for i in range(50):
            fn = random.choice(first_names)
            ln = random.choice(last_names)
            email = f"{fn.lower()}.{ln.lower()}{i}@example.com"
            phone = f"06{random.randint(10000000, 99999999)}"
            passport = f"{random.randint(10,99)}{random.choice(['AB','CD','EF','GH'])}{random.randint(10000,99999)}"
            year = random.randint(1970, 2005)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            dob = date(year, month, day)

            passenger, created = Passenger.objects.get_or_create(
                email=email,
                defaults={
                    'first_name': fn,
                    'last_name': ln,
                    'phone': phone,
                    'passport_number': passport,
                    'date_of_birth': dob,
                }
            )
            passengers.append(passenger)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created passenger: {passenger}'))

        self.stdout.write('Creating bookings...')

        meals = list(Meal.objects.filter(is_active=True))
        flights = list(Flight.objects.filter(status='SCHEDULED', available_seats__gt=0))

        def unique_ref():
            import string
            ref = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            while Booking.objects.filter(booking_reference=ref).exists():
                ref = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            return ref

        created_count = 0
        for i in range(50):
            if not flights:
                break
            flight = random.choice(flights)
            if flight.available_seats <= 0:
                flights.remove(flight)
                continue

            passenger = random.choice(passengers)
            meal = random.choice(meals) if meals else None
            num = 1
            if flight.available_seats < num:
                flights.remove(flight)
                continue

            booking = Booking.objects.create(
                booking_reference=unique_ref(),
                flight=flight,
                passenger=passenger,
                number_of_passengers=num,
                total_price=flight.price * num + ((meal.price if meal else 0) * num),
                status='CONFIRMED',
                meal=meal,
                description=(meal.description if meal else '')
            )
            created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully populated database! Created {created_count} bookings.'))
