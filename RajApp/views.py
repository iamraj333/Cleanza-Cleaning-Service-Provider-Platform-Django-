from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, BookingDataBase, Booking, ResidentalCleaning, KitchenCleaning,BathroomCleaning,OfficeCleaning,GardenCleaning,TreeCleaning,SofaCleaning,WindowCleaning,Post_ConstructionCleaning,CustomerFeedback, CleanzaCommunity,ContactUs, UserSetting,CleanzaBlog
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime
from django.core.mail import EmailMessage, send_mail #help to send main
from django.conf import settings

#importing modules for storing data in models which was coming from template .html
from django.http import HttpResponse, JsonResponse #giving response in json formate
from django.views.decorators.csrf import csrf_exempt #executing csrf protocol
import json #taking data in json formate

import random
from datetime import date

# Create your views here.
# def Intro(request):
#     return HttpResponse("<h1>Hello World</h1>")

# def Fun(request):
#     context={
#         "name":"Rajkumar"
#     }
#     return render(request, 'intro.html', context)


CleaningServices={
        "residentialCleaning": [
    {
      "id":1,
      "title": "Basic Home Cleaning",
      "imageUrl": "https://images.pexels.com/photos/6195125/pexels-photo-6195125.jpeg",
      "startingPrice": "₹1,499/Visit",
      "description": "Quick and reliable cleaning to keep your home fresh and tidy.",
      "about": "Basic Home Cleaning is a convenient service designed to keep your home neat, organized, and hygienic on a regular basis. Perfect for busy households, this service focuses on essential cleaning tasks that maintain overall cleanliness and freshness without requiring extensive deep cleaning. Our trained professionals handle dusting of surfaces, sweeping and mopping floors, and cleaning kitchens and bathrooms to ensure your home feels comfortable and welcoming. Routine cleaning prevents dust buildup, reduces allergens, and maintains a healthy living environment. This service is ideal for homeowners who need quick, reliable cleaning to complement their regular maintenance routines. Basic Home Cleaning can be customized to fit your home's size, layout, and specific cleaning needs. Whether it’s preparing your home for guests, maintaining hygiene in high-traffic areas, or simply enjoying a consistently tidy space, this service provides a time-saving, efficient solution. By entrusting your home to experienced cleaners, you can focus on your daily activities while ensuring a clean and organized environment.",
      "features": [
        "Floor sweeping & mopping",
        "Surface dusting",
        "Kitchen & bathroom cleaning"
      ],
      "servicesIncluded": [
        "Sweeping and mopping floors",
        "Dusting furniture and surfaces",
        "Cleaning kitchen counters and sink",
        "Bathroom cleaning and sanitization",
        "Trash collection and disposal",
        "Tidying bedrooms and living areas"
      ],
      "checklist": [
        {
          "task": "Dusting of all surfaces",
          "details": "Dusting and wiping of furniture, shelves, light fixtures, and other accessible surfaces to remove dirt and allergens."
        },
        {
          "task": "Floor cleaning",
          "details": "Sweeping, vacuuming, and mopping of all floors to remove dust, stains, and debris."
        },
        {
          "task": "Kitchen cleaning",
          "details": "Cleaning of kitchen countertops, sinks, stovetops, and exterior surfaces of appliances to maintain hygiene."
        },
        {
          "task": "Bathroom cleaning",
          "details": "Cleaning and sanitizing of sinks, toilets, mirrors, showers, and bathroom surfaces."
        },
        {
          "task": "Trash disposal",
          "details": "Collection and disposal of trash from all rooms, including replacing trash liners."
        },
        {
          "task": "Advance UV light cleaning",
          "details": "Use of advanced UV light technology to disinfect surfaces and reduce bacteria, viruses, and other harmful microorganisms."
        }
      ],
      "relatedServices": [2,3],
      "notes": "Ideal for weekly or regular cleaning schedules.",
      "timeRequired": "2-3 hours",
      "buttonText": "Schedule Cleaning"
    },
    {
      "id":2,
      "title": "Deep Home Cleaning",
      "imageUrl": "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=1200&h=800&fit=crop",
      "startingPrice": "₹3,999/Visit",
      "description": "A detailed top-to-bottom clean for a healthier home.",
      "about": "Deep Home Cleaning is a thorough cleaning service that targets hidden dirt, grime, and allergens in every corner of your home. Unlike routine cleaning, it involves an intensive approach to kitchens, bathrooms, floors, corners, tiles, switches, and other hard-to-reach areas. Deep cleaning improves indoor air quality, reduces allergens, and ensures your home is hygienic and safe for family members. This service is perfect for homes after renovations, seasonal cleaning, or for those who want an exceptionally clean environment. Trained cleaning professionals use safe yet effective products and systematic methods to deliver comprehensive results. Deep Home Cleaning also helps maintain the longevity of surfaces, furniture, and appliances by removing accumulated dirt that can cause wear over time. This service ensures your home not only looks clean but feels fresh, healthy, and well-maintained for all residents.",
      "features": [
        "Deep kitchen & bathroom cleaning",
        "Stain & grime removal",
        "Corners, tiles & switches"
      ],
      "servicesIncluded": [
        "Deep scrubbing of floors and tiles",
        "Kitchen countertop and appliance cleaning",
        "Bathroom and toilet sanitization",
        "Dusting corners, vents, and ceiling fans",
        "Cleaning switches and door handles",
        "Removal of stains and grime from surfaces"
      ],
      "checklist": [
        {
          "task": "Deep kitchen cleaning",
          "details": "Thorough cleaning of all kitchen surfaces, appliances, cabinets, and countertops to remove grease, grime, and food residues."
        },
        {
          "task": "Bathroom scrubbing",
          "details": "Complete scrubbing of sinks, toilets, showers, and tiles to remove soap scum, mold, and bacteria."
        },
        {
          "task": "Floor and tile cleaning",
          "details": "Sweeping, mopping, and scrubbing floors and tiles to remove dirt, stains, and buildup."
        },
        {
          "task": "Dusting of corners",
          "details": "Removal of dust and cobwebs from hard-to-reach areas, corners, ceiling edges, and behind furniture."
        },
        {
          "task": "Stain removal",
          "details": "Targeted treatment of stubborn stains on carpets, upholstery, and surfaces for a cleaner, fresher look."
        },
        {
          "task": "Advance UV light cleaning",
          "details": "Use of ultraviolet light to disinfect surfaces, kill bacteria, viruses, and other harmful microorganisms for a deeper clean."
        }
      ],
      "relatedServices": [1,9],
      "notes": "Recommended for monthly or quarterly deep cleaning schedules.",
      "timeRequired": "4-6 hours",
      "buttonText": "Schedule Cleaning"
    },
    {
      "id":3,
      "title": "Kitchen Deep Cleaning",
      "imageUrl": "https://images.pexels.com/photos/6195118/pexels-photo-6195118.jpeg",
      "startingPrice": "₹1,999/Visit",
      "description": "Remove grease, oil, and dirt for a hygienic kitchen.",
      "about": "Kitchen Deep Cleaning is a specialized service focused on removing grease, oil, dirt, and bacteria from all kitchen surfaces, appliances, and storage areas. Kitchens are high-traffic areas that often accumulate hidden grime in countertops, sinks, cabinets, and stoves. This service ensures a hygienic cooking environment by thoroughly cleaning all surfaces and addressing areas often missed in routine cleaning. Our professional cleaners use safe, effective products and techniques to sanitize and degrease your kitchen while maintaining the integrity of your appliances and furniture. Regular kitchen deep cleaning not only promotes food safety but also extends the life of cabinets, countertops, and appliances. It is ideal for households preparing for events, after cooking-heavy periods, or for regular maintenance to prevent buildup. The result is a sparkling, sanitized, and organized kitchen ready for daily use.",
      "features": [
        "Stove & countertop cleaning",
        "Sink & backsplash sanitization",
        "Cabinet exterior cleaning"
      ],
      "servicesIncluded": [
        "Cleaning stove and oven exterior",
        "Sanitizing sink and backsplash",
        "Wiping cabinet exteriors",
        "Countertop degreasing",
        "Floor mopping and trash removal"
      ],
      "checklist": [
        {
          "task": "Stove cleaning",
          "details": "Thorough cleaning of stove surfaces, burners, and knobs to remove grease, food residue, and stains."
        },
        {
          "task": "Sink and backsplash sanitization",
          "details": "Deep cleaning and disinfecting of the sink and backsplash to remove dirt, grime, and bacteria."
        },
        {
          "task": "Cabinet exterior cleaning",
          "details": "Wiping and polishing of cabinet doors and handles to remove dust, fingerprints, and smudges."
        },
        {
          "task": "Advance UV light cleaning",
          "details": "Use of ultraviolet light to disinfect surfaces, killing bacteria, viruses, and other harmful microorganisms."
        }
      ],
      "relatedServices": [1,2],
      "notes": "Intensive grease removal may take longer for commercial kitchens.",
      "timeRequired": "1.5-2 hours",
      "buttonText": "Schedule Cleaning"
    },
    {
      "id":4,
      "title": "Bathroom and Toilet Cleaning",
      "imageUrl": "https://images.pexels.com/photos/6195120/pexels-photo-6195120.jpeg",
      "startingPrice": "₹799/bathroom",
      "description": "Deep cleaning and sanitization for sparkling bathrooms.",
      "about": "Bathroom & Toilet Cleaning is a specialized service aimed at maintaining the cleanliness, hygiene, and freshness of your bathrooms. Bathrooms are high-use areas that accumulate soap scum, grime, bacteria, and unpleasant odors if not cleaned regularly. This service ensures thorough cleaning and sanitization of toilets, basins, showers, tiles, and fixtures. Professional cleaners use safe disinfectants and scrubbing techniques to remove stains, lime scale, mold, and other buildup. Regular bathroom cleaning not only improves the appearance and smell of your bathroom but also contributes to a healthier living environment by reducing germs and bacteria. This service is ideal for households, shared apartments, or offices where multiple bathrooms need frequent maintenance. It ensures a sparkling, sanitized, and odor-free bathroom, promoting comfort and hygiene for all users.",
      "features": [
        "Toilet & basin disinfection",
        "Tile & grout cleaning",
        "Odour & bacteria removal"
      ],
      "servicesIncluded": [
        "Sanitizing toilets, basins, and showers",
        "Scrubbing tiles and grout",
        "Removing mold and soap scum",
        "Wiping mirrors and fixtures",
        "Trash disposal and floor cleaning"
      ],
      "checklist": [
        {
          "task": "Toilet and basin disinfection",
          "details": "Thorough cleaning and sanitization of toilets and basins to remove germs and bacteria."
        },
        {
          "task": "Tile scrubbing",
          "details": "Scrubbing of tiles to remove grime, soap scum, and stubborn stains."
        },
        {
          "task": "Odor removal",
          "details": "Elimination of unpleasant smells from bathrooms or surfaces using safe cleaning methods."
        },
        {
          "task": "Advance UV light cleaning",
          "details": "Use of ultraviolet light to disinfect surfaces, killing bacteria, viruses, and other harmful microorganisms."
        }
      ],
      "relatedServices": [1,2],
      "notes": "Price is per bathroom; multiple bathrooms may require more time.",
      "timeRequired": "1-1.5 hours per bathroom",
      "buttonText": "Schedule Cleaning"
    }
  ],
  "officeCommercialCleaning": [
    {
      "id":5,
      "title": "Office Cleaning",
      "imageUrl": "https://images.pexels.com/photos/3768911/pexels-photo-3768911.jpeg",
      "startingPrice": "₹2,499/Visit",
      "description": "Maintain a clean and professional workplace.",
      "about": "Office Cleaning is a routine maintenance service designed to keep workplaces clean, organized, and professional on a daily or scheduled basis. A clean office environment plays a crucial role in employee productivity, health, and morale. This service focuses on maintaining cleanliness in workstations, common areas, meeting rooms, pantries, and restrooms. Regular office cleaning helps reduce dust, germs, and clutter, creating a healthier workspace and minimizing the spread of illness among employees. It also enhances the professional appearance of your business, leaving a positive impression on clients and visitors. Our trained cleaning professionals follow systematic cleaning procedures using commercial-grade yet safe cleaning products. Office Cleaning is suitable for small offices, corporate spaces, co-working environments, and commercial establishments. While it does not involve intensive deep scrubbing, it ensures consistent hygiene and order. Regular office cleaning also extends the life of office furniture, flooring, and equipment by preventing dirt buildup. This service can be customized based on office size, working hours, and frequency requirements.",
      "features": [
        "Desks & workstations",
        "Floor & common area cleaning",
        "Restroom cleaning"
      ],
      "servicesIncluded": [
        "Desk and workstation dusting",
        "Chair and furniture cleaning",
        "Floor sweeping and mopping",
        "Carpet vacuuming",
        "Meeting room cleaning",
        "Reception area cleaning",
        "Pantry cleaning",
        "Restroom cleaning and sanitization",
        "Trash collection and disposal"
      ],
      "checklist": [
        {
          "task": "Desk and chair dusting",
          "details": "Removal of dust and debris from desks, chairs, and other furniture to keep surfaces clean."
        },
        {
          "task": "Floor sweeping and mopping",
          "details": "Sweeping and mopping of all floors to remove dirt, stains, and maintain hygiene."
        },
        {
          "task": "Pantry surface cleaning",
          "details": "Wiping and sanitizing pantry shelves and counters to remove crumbs, spills, and dust."
        },
        {
          "task": "Restroom cleaning",
          "details": "Complete cleaning and disinfecting of sinks, toilets, and floors to ensure a hygienic restroom."
        },
        {
          "task": "Waste disposal",
          "details": "Emptying trash bins and disposing of waste safely and hygienically."
        },
        {
          "task": "UV light Sanitation",
          "details": "Use of ultraviolet light to disinfect surfaces, killing bacteria, viruses, and other harmful microorganisms."
        }
      ],
      "relatedServices": [6,10],
      "notes": "Cleaning schedules can be customized for daily, weekly, or monthly service.",
      "timeRequired": "3-4 hours",
      "buttonText": "Schedule Cleaning"
    },
    {
      "id":6,
      "title": "Office Deep Cleaning",
      "imageUrl": "https://images.unsplash.com/photo-1604014237800-1c9102c219da?w=1200&h=800&fit=crop",
      "startingPrice": "₹6,999/Visit",
      "description": "Complete cleaning for a healthier work environment.",
      "about": "Office Deep Cleaning is a comprehensive cleaning service designed to eliminate deeply embedded dirt, germs, and bacteria from office spaces. Unlike routine office cleaning, this service focuses on intensive cleaning of floors, carpets, workstations, high-touch surfaces, and less accessible areas. It is highly recommended periodically, after renovations, or during seasonal hygiene upgrades. Office Deep Cleaning improves indoor air quality, reduces allergens, and creates a healthier and safer working environment for employees. Our professional team uses specialized equipment and professional-grade cleaning solutions to ensure thorough sanitization. This service is especially beneficial for offices with high foot traffic, shared workspaces, and client-facing areas. Deep cleaning also helps restore the appearance of office interiors, making them look refreshed and well-maintained. While it requires more time than routine cleaning, the long-term hygiene benefits make it a valuable investment. Office Deep Cleaning supports workplace wellness, compliance with hygiene standards, and employee satisfaction.",
      "features": [
        "Deep floor & carpet cleaning",
        "High-touch surface sanitization",
        "Pantry & restroom deep clean"
      ],
      "servicesIncluded": [
        "Deep floor scrubbing",
        "Carpet shampooing",
        "Workstation deep cleaning",
        "Door handle and switch sanitization",
        "Pantry degreasing",
        "Restroom deep sanitization",
        "Corner and edge dust removal",
        "Furniture surface cleaning"
      ],
      "checklist": [
        {
          "task": "Carpet and floor deep cleaning",
          "details": "Thorough cleaning of carpets and floors to remove dirt, stains, and allergens."
        },
        {
          "task": "High-touch surface sanitization",
          "details": "Disinfecting frequently touched surfaces like doorknobs, switches, and handles to reduce germs."
        },
        {
          "task": "Pantry deep cleaning",
          "details": "Intensive cleaning of pantry shelves, counters, and storage areas to remove dust and spills."
        },
        {
          "task": "Restroom sanitization",
          "details": "Complete cleaning and disinfecting of toilets, sinks, and floors for a hygienic restroom."
        },
        {
          "task": "Corner dust removal",
          "details": "Removal of dust and cobwebs from corners, edges, and hard-to-reach areas."
        },
        {
          "task": "UV light Sanitization",
          "details": "Use of ultraviolet light to disinfect surfaces, killing bacteria, viruses, and other harmful microorganisms."
        }
      ],
      "relatedServices": [5,11],
      "notes": "Best scheduled during non-working hours to avoid disruption.",
      "timeRequired": "6-8 hours",
      "buttonText": "Schedule Cleaning"
    }
  ],
  "outdoorGardenServices": [
    {
      "id":7,
      "title": "Garden Cleaning",
      "imageUrl": "https://images.pexels.com/photos/4505168/pexels-photo-4505168.jpeg",
      "startingPrice": "₹1,499/Visit",
      "description": "Keep your garden neat and well-maintained.",
      "about": "Garden Cleaning is a professional service designed to maintain the cleanliness, organization, and aesthetic appeal of your outdoor spaces. A well-maintained garden not only enhances the beauty of your home but also provides a safe and enjoyable environment for relaxation, recreation, and family activities. This service focuses on removing leaves, debris, weeds, fallen branches, and other unwanted materials that accumulate over time. It includes cleaning pathways, patios, lawns, flower beds, and other outdoor areas to ensure a tidy appearance. Regular garden cleaning also helps prevent pest infestations, promotes healthy plant growth, and reduces the risk of accidents caused by cluttered or slippery surfaces. Our trained team uses the appropriate tools and eco-friendly cleaning methods to ensure thorough maintenance without harming plants or the environment. This service is ideal for homeowners, property managers, and anyone who wants a neat and inviting outdoor space without the hassle of manual upkeep. Whether you have a small backyard or a large garden, our team ensures consistent care and attention to every corner of your outdoor area, leaving it fresh, safe, and visually appealing.",
      "features": [
        "Leaf & debris removal",
        "Pathway & outdoor cleaning",
        "Waste disposal"
      ],
      "servicesIncluded": [
        "Leaf collection and disposal",
        "Removal of dead plants and weeds",
        "Clearing garden pathways",
        "Patio and deck sweeping",
        "Cleaning around fountains or ponds",
        "Trimming small shrubs",
        "Waste collection and disposal",
        "Mulch or soil replacement (if required)",
        "General area tidying and raking"
      ],
      "checklist": [
        {
          "task": "Leaf and debris removal",
          "details": "Clearing leaves, twigs, and other debris from lawns, gardens, and pathways."
        },
        {
          "task": "Pathway cleaning",
          "details": "Sweeping and washing pathways to remove dirt, moss, and litter for safe and clean walkways."
        },
        {
          "task": "Waste collection",
          "details": "Collecting garden waste and disposing of it properly to maintain a tidy outdoor space."
        },
        {
          "task": "Sweeping and raking of garden",
          "details": "Raking leaves and debris from lawns and garden beds and sweeping hard surfaces for a neat appearance."
        },
        {
          "task": "General tidy-up of outdoor space",
          "details": "Organizing and cleaning outdoor areas, including furniture, tools, and decorative elements."
        }
      ],
      "relatedServices": [8,11],
      "notes": "Landscaping, planting, or fertilization services are not included unless specifically requested.",
      "timeRequired": "2-3 hours",
      "buttonText": "Schedule Cleaning"
    },
    {
      "id":8,
      "title": "Tree Cutting and Trimming",
      "imageUrl": "https://images.pexels.com/photos/2132250/pexels-photo-2132250.jpeg",
      "startingPrice": "₹2,999/Visit",
      "description": "Safe and professional tree care services.",
      "about": "Tree Cutting and Trimming is a specialized outdoor service focused on maintaining the health, safety, and aesthetic appeal of trees in your garden, lawn, or commercial property. Overgrown, damaged, or unsafe branches can pose risks to people, property, and other plants. This service provides safe and professional removal of such branches, as well as trimming to shape and maintain trees according to health and design requirements. Our experienced team assesses each tree individually and uses proper techniques and safety equipment to ensure precise cutting and trimming. The service also includes cleaning and disposal of all cut branches and debris, leaving your outdoor space clean and hazard-free. Regular tree maintenance improves sunlight exposure for surrounding plants, encourages healthy growth, and prevents disease spread among trees. Ideal for residential and commercial properties, this service ensures that your trees remain visually appealing, structurally sound, and safe throughout the year. Additionally, professional trimming enhances property value and supports long-term garden sustainability.",
      "features": [
        "Tree trimming & shaping",
        "Overgrown branch removal",
        "Clean-up included"
      ],
      "servicesIncluded": [
        "Tree inspection and assessment",
        "Pruning and shaping branches",
        "Removal of dead or overgrown limbs",
        "Safe disposal of cut branches",
        "Ground-level debris cleanup",
        "Trimming hedges around trees",
        "Ensuring safe clearance from structures",
        "Removal of obstructive branches"
      ],
      "checklist": [
        {
          "task": "Inspection of trees",
          "details": "Examining trees for health, disease, or structural issues to ensure safety and proper growth."
        },
        {
          "task": "Safe branch cutting",
          "details": "Trimming branches carefully to remove dead or overgrown limbs while maintaining tree health and safety."
        },
        {
          "task": "Shape correction",
          "details": "Pruning trees to improve their shape, structure, and overall appearance."
        },
        {
          "task": "Area cleanup",
          "details": "Removing fallen branches, leaves, and debris from the surrounding area for a tidy environment."
        },
        {
          "task": "Waste disposal",
          "details": "Collecting and disposing of tree waste safely and responsibly."
        }
      ],
      "relatedServices": [7,11],
      "notes": "Full tree removal may require additional assessment and approval. Specialized equipment may be needed for very tall trees.",
      "timeRequired": "3-5 hours",
      "buttonText": "Schedule Cleaning"
    }
  ],
  "specialisedCleaning": [
    {
      "id":9,
      "title": "Sofa and Carpet Cleaning",
      "imageUrl": "https://images.pexels.com/photos/6195122/pexels-photo-6195122.jpeg",
      "startingPrice": "₹1,299/Visit",
      "description": "Deep cleaning to remove dirt, stains, and allergens.",
      "about": "Sofa and Carpet Cleaning is a specialized service designed to thoroughly clean fabric and upholstered surfaces in homes and offices. Over time, sofas and carpets accumulate dust, allergens, pet hair, food spills, and deep-seated dirt that cannot be removed through routine vacuuming. This service targets these hidden contaminants using fabric-safe cleaning agents, steam cleaning, and professional-grade equipment to restore freshness and hygiene. Regular cleaning of sofas and carpets not only enhances the appearance of your furniture and flooring but also prolongs their lifespan by preventing fiber deterioration. It is particularly beneficial for households with children, pets, or allergy-prone individuals, as it reduces the presence of dust mites, bacteria, and unpleasant odours. Our trained professionals carefully handle delicate fabrics to prevent damage while delivering effective cleaning results. The service includes quick-drying techniques to minimize downtime, allowing you to use your furniture and floors shortly after cleaning. Ideal for routine maintenance, post-party cleaning, or seasonal deep cleaning, Sofa and Carpet Cleaning ensures a cleaner, healthier, and more inviting living environment while maintaining the aesthetic appeal of your home or office.",
      "features": [
        "Fabric-safe cleaning",
        "Stain & odour removal",
        "Quick drying"
      ],
      "servicesIncluded": [
        "Vacuuming of sofa and carpet",
        "Spot treatment of stains",
        "Fabric-safe shampooing",
        "Odour neutralization",
        "Steam cleaning",
        "Edge and corner cleaning",
        "Pet hair and dust removal",
        "Quick drying of fabrics",
        "Final inspection and touch-up"
      ],
      "checklist": [
        {
          "task": "Dust and dirt extraction",
          "details": "Removing embedded dust, dirt, and debris from carpets, upholstery, and fabrics for a cleaner surface."
        },
        {
          "task": "Stain removal",
          "details": "Treating and eliminating stains from carpets, rugs, and upholstery to restore appearance."
        },
        {
          "task": "Odor neutralization",
          "details": "Eliminating unpleasant smells from fabrics and surfaces for a fresh, clean environment."
        },
        {
          "task": "Steam cleaning",
          "details": "Using high-temperature steam to deep clean and sanitize surfaces without harsh chemicals."
        },
        {
          "task": "Quick drying",
          "details": "Ensuring cleaned surfaces dry rapidly to prevent moisture damage and allow immediate use."
        }
      ],
      "relatedServices": [2,11],
      "notes": "Cleaning time may vary depending on size and number of sofas/carpets.",
      "timeRequired": "1.5-2 hours",
      "buttonText": "Schedule Cleaning"
    },
    {
      "id":10,
      "title": "Window and Glass Cleaning",
      "imageUrl": "https://images.pexels.com/photos/9462101/pexels-photo-9462101.jpeg",
      "startingPrice": "₹999/Visit",
      "description": "Crystal-clear windows for homes and offices.",
      "about": "Window and Glass Cleaning is a service dedicated to achieving streak-free, sparkling clean windows and glass surfaces in both residential and commercial spaces. Dust, smudges, fingerprints, watermarks, and pollution buildup can make windows look dull and unhygienic. This service involves cleaning interior and exterior glass, frames, and sills using specialized techniques and safe cleaning solutions to restore transparency and shine. Clean windows not only enhance the aesthetic appeal of your home or office but also improve natural light, visibility, and overall atmosphere. Regular window cleaning reduces the risk of mold and dirt accumulation, ensuring a healthier indoor environment. The service can be customized for high-rise buildings, difficult-to-reach areas, and glass partitions. Professional cleaners follow safety protocols to deliver quality results efficiently. Ideal for offices, apartments, and homes, Window and Glass Cleaning contributes to a polished, welcoming, and professional appearance while maintaining long-term clarity and hygiene of glass surfaces.",
      "features": [
        "Interior & exterior glass",
        "Streak-free finish",
        "Frame cleaning"
      ],
      "servicesIncluded": [
        "Cleaning of interior and exterior windows",
        "Frame and sill wiping",
        "Removal of dust, dirt, and water spots",
        "Streak-free polishing",
        "Glass partitions cleaning",
        "High-rise or hard-to-reach window cleaning"
      ],
      "checklist": [
        {
          "task": "Interior window cleaning",
          "details": "Cleaning the inside surfaces of windows to remove dust, fingerprints, and smudges."
        },
        {
          "task": "Exterior window cleaning",
          "details": "Cleaning the outside surfaces of windows to remove dirt, grime, and environmental residues."
        },
        {
          "task": "Frame cleaning",
          "details": "Wiping and sanitizing window frames, sills, and tracks for a complete clean."
        },
        {
          "task": "Streak-free finish",
          "details": "Polishing glass surfaces to ensure a clear, streak-free shine."
        },
        {
          "task": "Glass partition cleaning",
          "details": "Cleaning glass partitions in offices or rooms to remove dust, fingerprints, and smudges."
        }
      ],
      "relatedServices": [5,2],
      "notes": "High-rise or large windows may require additional time and equipment.",
      "timeRequired": "1-2 hours",
      "buttonText": "Schedule Cleaning"
    },
    {
      "id":11,
      "title": "Post-Construction Cleaning",
      "imageUrl": "https://images.pexels.com/photos/31983864/pexels-photo-31983864.jpeg",
      "startingPrice": "₹7,999/Visit",
      "description": "Make your space move-in ready after construction.",
      "about": "Post-Construction Cleaning is a comprehensive service designed to clean homes, offices, or commercial spaces after construction or renovation work. These spaces often have layers of dust, debris, paint splatters, and leftover building materials that require professional cleaning to make them safe, hygienic, and ready for occupancy. The service involves dusting, vacuuming, scrubbing floors, walls, windows, and fixtures, removing cement and paint residues, and ensuring all areas are spotless. It also addresses hidden dirt in corners, vents, and high surfaces that may be missed during regular cleaning. Post-Construction Cleaning improves air quality, removes allergens, and ensures the space is visually appealing and ready for immediate use. It is ideal for newly built homes, remodeled offices, or commercial properties. Our team uses professional equipment, effective cleaning agents, and systematic methods to ensure thorough cleaning while maintaining safety standards. This service saves time, reduces stress, and ensures a smooth transition from construction to occupancy, leaving your space sparkling, safe, and move-in ready.",
      "features": [
        "Dust & debris removal",
        "Paint & cement residue cleaning",
        "Full area cleaning"
      ],
      "servicesIncluded": [
        "Removal of construction dust and debris",
        "Cleaning walls, ceilings, and floors",
        "Window and glass cleaning",
        "Cabinet and fixture cleaning",
        "Sanitizing bathrooms and kitchens",
        "Vacuuming and mopping all areas",
        "Scrubbing tiles and grout",
        "Disposal of leftover construction materials"
      ],
      "checklist": [
        {
          "task": "Dust and debris removal",
          "details": "Clearing dust, construction debris, and leftover materials from all areas for a clean workspace."
        },
        {
          "task": "Paint and cement residue cleaning",
          "details": "Removing paint splashes, cement residue, and other stubborn construction marks from surfaces."
        },
        {
          "task": "Full area cleaning",
          "details": "Thorough cleaning of all rooms and surfaces to make the space ready for use."
        },
        {
          "task": "Bathroom sanitization",
          "details": "Deep cleaning and disinfecting of bathroom fixtures, tiles, and floors."
        },
        {
          "task": "Kitchen deep cleaning",
          "details": "Cleaning and sanitizing kitchen surfaces, appliances, counters, and cabinets."
        },
        {
          "task": "Advance UV light Cleaning",
          "details": "Using ultraviolet light to disinfect surfaces, eliminating bacteria, viruses, and other harmful microorganisms."
        }
      ],
      "relatedServices": [2,6],
      "notes": "Ideal for post-renovation or new property cleaning. May require multiple cleaners for large spaces.",
      "timeRequired": "6-10 hours",
      "buttonText": "Schedule Cleaning"
    }
  ],
  "dailyCleaning": [
    {
      "id":12,
      "title": "Daily Home Cleaning",
      "imageUrl": "https://images.pexels.com/photos/6195125/pexels-photo-6195125.jpeg",
      "startingPrice": "₹14,999/month",
      "description": "Keep your home consistently clean and fresh with daily professional cleaning services.",
      "about": "Daily Home Cleaning is a subscription-based service designed for households that want their homes maintained at a consistently high standard without worrying about daily chores. Our trained cleaning professionals visit your home every day to ensure floors, kitchens, bathrooms, bedrooms, and common areas remain spotless, hygienic, and organized. This service not only keeps your home looking neat and welcoming but also helps prevent dirt buildup, reduces allergens, and prolongs the life of furniture, flooring, and fixtures. Daily Home Cleaning is ideal for busy families, working professionals, or anyone who values a consistently clean and healthy living environment. The service includes routine dusting, sweeping, mopping, trash disposal, and basic kitchen and bathroom cleaning. Our team can also perform additional tasks such as laundry folding, bed making, and tidying up toys or workspaces, customized according to your needs. With Daily Home Cleaning, your home will always feel fresh and inviting, saving you time and effort while promoting a healthier lifestyle.",
      "features": [
        "Daily floor sweeping & mopping",
        "Daily surface dusting",
        "Daily kitchen & bathroom cleaning"
      ],
      "servicesIncluded": [
        "Daily dusting of all rooms",
        "Vacuuming and mopping floors",
        "Daily kitchen counter and sink cleaning",
        "Bathroom cleaning and sanitization",
        "Trash collection and disposal",
        "Tidying bedrooms and living areas",
        "Making beds and arranging furniture",
        "Wiping door handles and switches",
        "Light laundry folding and organizing"
      ],
      "checklist": [
        {
          "task": "Dusting of all surfaces",
          "details": "Removing dust from furniture, shelves, electronics, and other surfaces for a clean environment."
        },
        {
          "task": "Floor sweeping/mopping",
          "details": "Sweeping and mopping all floors to remove dirt, spills, and maintain hygiene."
        },
        {
          "task": "Bathroom cleaning",
          "details": "Cleaning and disinfecting sinks, toilets, showers, and floors for a hygienic bathroom."
        },
        {
          "task": "Kitchen counters wiped",
          "details": "Wiping and sanitizing kitchen counters and surfaces to remove food residues and spills."
        },
        {
          "task": "Trash disposal",
          "details": "Emptying trash bins and disposing of waste safely and hygienically."
        },
        {
          "task": "UV light Sanitation (2 times a month)",
          "details": "Using ultraviolet light twice a month to disinfect surfaces, killing bacteria, viruses, and other harmful microorganisms."
        }
      ],
      "relatedServices": [1,13],
      "notes": "Price based on daily visits 5-6 days a week. Additional services may incur extra charges.",
      "timeRequired": "3-4 hours per day",
      "buttonText": "Subscribe Now"
    },
    {
      "id":13,
      "title": "Daily Office Cleaning",
      "imageUrl": "https://images.pexels.com/photos/3768911/pexels-photo-3768911.jpeg",
      "startingPrice": "₹24,999/month",
      "description": "Maintain a clean and hygienic office space every day with professional cleaning.",
      "about": "Daily Office Cleaning is a subscription service aimed at keeping commercial and office spaces consistently clean, organized, and professional. Offices experience high foot traffic, shared workspaces, and frequent use of common areas, making daily cleaning essential for hygiene and productivity. Our trained professionals visit your office every day to perform dusting, floor cleaning, restroom sanitization, workstation maintenance, and common area tidying. This service reduces the risk of germs, allergens, and unpleasant odours, ensuring a healthier environment for employees, clients, and visitors. Daily Office Cleaning helps maintain a professional image, prolongs the lifespan of office furniture, carpets, and equipment, and creates a positive working atmosphere. The service can be tailored to include pantry cleaning, window wiping, and light organizational tasks based on your office requirements. With a daily cleaning schedule, offices remain fresh, inviting, and ready for operation at all times, reducing the need for intensive deep cleaning sessions and enhancing overall workplace satisfaction.",
      "features": [
        "Daily desks & workstations",
        "Daily floor & common area cleaning",
        "Daily restroom cleaning"
      ],
      "servicesIncluded": [
        "Daily dusting of desks and workstations",
        "Vacuuming and floor mopping",
        "Sanitization of restrooms",
        "Cleaning of common areas and reception",
        "Pantry cleaning and counter wiping",
        "Trash collection and disposal",
        "Door handles and switch sanitization",
        "Window and glass spot cleaning",
        "Tidying conference rooms and meeting spaces"
      ],
      "checklist": [
        {
          "task": "Desk and workstation dusting",
          "details": "Removing dust from desks, workstations, keyboards, and office equipment for a clean workspace."
        },
        {
          "task": "Floor cleaning",
          "details": "Sweeping, mopping, or vacuuming floors to remove dirt and maintain hygiene."
        },
        {
          "task": "Restroom sanitization",
          "details": "Cleaning and disinfecting sinks, toilets, and floors to ensure a hygienic restroom."
        },
        {
          "task": "Trash disposal",
          "details": "Emptying trash bins and disposing of office waste safely and responsibly."
        },
        {
          "task": "Common area tidying",
          "details": "Organizing and cleaning shared spaces such as lounges, corridors, and meeting rooms."
        },
        {
          "task": "Advance UV light cleaning (2 times a month)",
          "details": "Using ultraviolet light twice a month to disinfect surfaces, killing bacteria, viruses, and other harmful microorganisms."
        }
      ],
      "relatedServices": [12,5],
      "notes": "Price is based on daily cleaning 5-6 days a week. Additional services or weekends may be extra.",
      "timeRequired": "4-5 hours per day",
      "buttonText": "Subscribe Now"
    }
  ],
  "customizedCleaning":[
    {
      "id":14,
      "title": "Specialized Cleaning",
      "imageUrl": "https://images.pexels.com/photos/8293635/pexels-photo-8293635.jpeg",
      "startingPrice": "₹10,000/visit",
      "description": "Customized cleaning service based on your checklist.",
      "about": "Our Customized Cleaning Service is designed to give you full control over how your space is maintained, allowing you to choose the tasks and areas that matter most. Whether it’s workstations, floors, restrooms, common areas, or optional extras like window cleaning and UV surface disinfection, you decide what gets cleaned and how often. This flexibility ensures that every corner of your office, home, or shared space receives the attention it needs without paying for unnecessary services. Our trained professionals use high-quality cleaning products and techniques to maintain hygiene, remove dust, and create a fresh, welcoming environment tailored specifically to your preferences. With customizable schedules, frequency options, and add-on services, we make maintaining cleanliness simple and stress-free. Experience a cleaner, healthier, and more organized space that reflects your exact requirements, saving time while promoting comfort, productivity, and well-being for everyone who uses it.",
      "features": [
        "Client‑defined cleaning tasks",
        "Daily floor & common area cleaning",
        "Thorough attention to detail"
      ],
      "servicesIncluded": [
        "Daily dusting of desks, workstations, and shelves",
        "Vacuuming, sweeping, and floor mopping",
        "Sanitization of restrooms including sinks, toilets, and mirrors",
        "Pantry and kitchen area cleaning, counter wiping, and appliance exterior cleaning",
        "Door handles, light switches, and elevator button sanitization",
        "Window, glass, and mirror spot cleaning",
      ],
      "checklist": [
        {
          "task": "Workspace dusting",
          "details": "Users can choose which desks, shelves, and equipment to dust and wipe down for a personalized clean."
        },
        {
          "task": "Floor care",
          "details": "Users select areas for sweeping, mopping, or vacuuming according to their space and flooring type."
        },
        {
          "task": "Restroom cleaning",
          "details": "Users decide which restrooms to sanitize, including sinks, toilets, and mirrors, with their preferred cleaning intensity."
        },
        {
          "task": "Trash management",
          "details": "Users pick which bins to empty, including recycling and general waste, for a customized trash disposal routine."
        },
        {
          "task": "Common area upkeep",
          "details": "Users select shared spaces to tidy, such as lounges, reception areas, or meeting rooms, including dusting and organizing furniture."
        },
        {
          "task": "Optional extra services",
          "details": "Users can choose additional services such as UV surface disinfection, window cleaning, pantry cleaning, or high-touch surface sanitization."
        }
      ],
      "relatedServices": [1,5],
      "notes": "Cleaning schedules can be customized for daily, weekly, or monthly service",
      "timeRequired": "3-4 hours",
      "buttonText": "Schedule Cleaning"
    }
  ]
}


# Pricing
PricingPlan={
  "plans": [
    {
      "name": "Basic Plan",
      "tagline": "Best for light cleaning & small households",
      "price": "₹5,999",
      "perfectFor": "Studio apartments & 1 BHK homes. Ideal for individuals, couples, or low-usage homes looking for affordable, regular upkeep.",
      "about": "The Basic Plan covers essential cleaning tasks to maintain daily hygiene and cleanliness. It includes basic UV sanitization for frequently touched surfaces—keeping germs in check without heavy cleaning.",
      "includes": [
        "Floor sweeping & mopping",
        "Dusting of furniture & open surfaces",
        "Kitchen counter & sink cleaning",
        "Bathroom cleaning (toilet & washbasin)",
        "UV light sanitization for high-touch areas"
      ],
      "serviceFrequency": {
        "visitsPerWeek": 2,
        "hoursPerVisit": "1.5-2"
      }
    },
    {
      "name": "Standard Plan",
      "tagline": "Most Popular. Best for families & complete regular cleaning",
      "price": "₹9,999",
      "perfectFor": "2–3 BHK homes & families. Great for households with children, pets, or higher daily usage.",
      "about": "The Standard Plan offers a balanced mix of routine cleaning and deep care. With extended coverage and room-level UV sanitization, it ensures a healthier, fresher living environment.",
      "includes": [
        "Everything in the Basic Plan",
        "Deep kitchen cleaning (stove, sink & tiles)",
        "Deep bathroom cleaning (tiles, fittings & floors)",
        "Window & balcony cleaning (once per month)",
        "UV light sanitization for rooms, kitchen & bathrooms"
      ],
      "serviceFrequency": {
        "visitsPerWeek": 3,
        "hoursPerVisit": "2–3"
      }
    },
    {
      "name": "Premium Plan",
      "tagline": "Best for luxury homes & total hygiene care",
      "price": "₹34,999",
      "perfectFor": "Villas, large homes, offices & premium properties",
      "about": "The Premium Plan is a complete, worry-free solution with daily professional cleaning and advanced sanitization. Designed for those who want spotless cleanliness and maximum hygiene—without lifting a finger.",
      "includes": [
        "Everything in the Standard Plan",
        "Daily cleaning (Monday to Saturday)",
        "Sofa & mattress vacuum cleaning",
        "Kitchen cabinet exterior cleaning",
        "Interior glass & window cleaning",
        "Priority customer support",
        "Advanced UV sanitization for the entire home"
      ],
      "serviceFrequency": {
        "visitsPerWeek": 6,
        "hoursPerVisit": "3–4"
      }
    }
  ]
}


#blogs data
blogData = [
  {
    "id":1,
    "title": "10 Smart Cleaning Tips to Maintain a Hygienic Home",
    "image_url": "https://images.unsplash.com/photo-1581578731548-c64695cc6952",
    "author": "Ananya Mehta",
    "date_of_written": "2026-01-05",
    "read_time": "3 min",
    "category": "tips and tricks",
    "tags": ["home cleaning","daily hygiene","clean home","cleaning routine"],
    "content": """
    Maintaining a hygienic home is essential for good health, but it does not need to be complicated or time-consuming. A few simple habits practiced consistently can keep your home fresh and free from harmful germs.

    One effective approach is focusing on high-touch surfaces. Door handles, light switches, mobile phones, and kitchen counters collect bacteria quickly. Cleaning these areas daily with a disinfectant wipe or spray can significantly reduce the spread of germs. Microfiber cloths are especially useful because they trap dust and bacteria more effectively than traditional cloth.

    Another important tip is to clean as you go. Instead of allowing dishes, laundry, or clutter to pile up, handling small tasks throughout the day makes cleaning manageable. This habit also prevents dirt buildup that can later require deep cleaning.

    Ventilation also plays an important role in hygiene. Opening windows for 15–20 minutes daily improves air circulation and reduces moisture that can cause mold growth. In bathrooms and kitchens especially, proper airflow prevents unpleasant odors and bacteria buildup.

    Finally, remember to keep cleaning tools themselves clean. Dirty sponges, mops, and cloths can spread bacteria rather than remove it. Wash reusable cloths regularly and replace worn-out tools. With these simple habits, maintaining a hygienic home becomes much easier and more sustainable.
    """
  },

  {
    "id":2,
    "title": "The Importance of Kitchen Hygiene in Everyday Life",
    "image_url": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f",
    "author": "Rahul Desai",
    "date_of_written": "2026-01-10",
    "read_time": "4 min",
    "category": "cleaning techniques",
    "tags": ["kitchen hygiene","food safety","clean kitchen","sanitation"],
    "content": """
    The kitchen is one of the most frequently used areas in any home, and it is also one of the places where bacteria can easily spread. Maintaining proper kitchen hygiene is essential for preventing food contamination and ensuring the health of everyone in the household.

    One of the first steps in maintaining kitchen cleanliness is separating raw and cooked foods. Cross-contamination can occur when cutting boards or utensils used for raw meat are not cleaned properly before being used for other ingredients. Using different boards for vegetables and meat helps minimize this risk.

    Cleaning kitchen surfaces immediately after cooking is another important habit. Food spills, grease, and crumbs can attract pests and bacteria if left unattended. Wiping surfaces with warm water and mild disinfectant keeps the area clean and safe.

    Another often overlooked aspect is cleaning kitchen appliances. Refrigerators, microwaves, and stovetops accumulate grime over time. Regularly removing expired food, wiping shelves, and cleaning appliance surfaces helps maintain hygiene and improves their lifespan.

    Finally, proper waste management is essential. Kitchen bins should be emptied regularly and cleaned to prevent odor and bacteria buildup. Practicing these hygiene habits ensures that the kitchen remains a safe and pleasant environment for preparing meals every day.
    """
  },

  {
    "id":3,
    "title": "Microfiber Cleaning Tools: A Modern Cleaning Innovation",
    "image_url": "https://images.unsplash.com/photo-1595514535215-9d98c9e0f2c8",
    "author": "Priya Sharma",
    "date_of_written": "2026-01-15",
    "read_time": "4 min",
    "category": "innovation",
    "tags": ["microfiber","cleaning technology","modern tools","eco cleaning"],
    "content": """
    Cleaning technology has advanced significantly over the past decade, and microfiber materials have become one of the most effective tools in modern cleaning. Microfiber cloths and mops are designed with extremely fine fibers that trap dust, dirt, and bacteria more efficiently than traditional cotton cloths.

    The secret behind microfiber lies in its structure. Each fiber is split into tiny strands that create a larger surface area capable of capturing microscopic particles. When used dry, microfiber attracts dust through static electricity. When damp, it can remove grease and stains without the need for strong chemical cleaners.

    Another advantage of microfiber cleaning tools is sustainability. Because they are reusable and durable, they reduce reliance on disposable paper towels and wipes. This not only saves money but also reduces environmental waste.

    Microfiber tools are widely used in hospitals and commercial cleaning services because of their ability to remove up to 99 percent of bacteria when used correctly. Their lightweight design also makes cleaning easier and faster.

    As people become more conscious about hygiene and environmental impact, microfiber technology continues to gain popularity in homes and professional cleaning environments around the world.
    """
  },

  {
    "id":4,
    "title": "Essential Cleaning Tools Every Home Should Own",
    "image_url": "https://images.unsplash.com/photo-1585421514738-01798e348b17",
    "author": "Neha Kapoor",
    "date_of_written": "2026-01-20",
    "read_time": "5 min",
    "category": "tools",
    "tags": ["cleaning equipment","home tools","cleaning kit","hygiene tools"],
    "content": """
    Having the right cleaning tools makes household cleaning easier and more effective. While basic cleaning supplies are common in most homes, certain tools can significantly improve cleaning efficiency and hygiene.

    A good vacuum cleaner is one of the most valuable cleaning tools. Modern vacuums with HEPA filters capture tiny dust particles and allergens, making them especially helpful for people with allergies. Regular vacuuming also helps maintain better indoor air quality.

    Another essential tool is a microfiber mop. Unlike traditional mops, microfiber versions use less water and capture dirt more effectively. They are suitable for multiple floor types including tiles, laminate, and hardwood.

    Scrub brushes are also important for deep cleaning. These brushes help remove stubborn stains from bathroom tiles, grout lines, and kitchen sinks where bacteria often accumulate. Pairing them with mild disinfectants improves results.

    A handheld steam cleaner is another useful tool. Steam cleaning uses high temperatures to eliminate germs without chemical cleaners, making it a safer option for homes with children and pets.

    By keeping a well-equipped cleaning kit, homeowners can maintain better hygiene while reducing the time and effort required for everyday cleaning tasks.
    """
  },

  {
    "id":5,
    "title": "How to Keep Your Bathroom Germ Free",
    "image_url": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3",
    "author": "Rohan Verma",
    "date_of_written": "2026-01-25",
    "read_time": "3 min",
    "category": "cleaning techniques",
    "tags": ["bathroom cleaning","germ free","bathroom hygiene"],
    "content": """
    Bathrooms are one of the most bacteria-prone areas in any home, making regular cleaning essential for maintaining hygiene. Because bathrooms are exposed to constant moisture, they create the perfect environment for bacteria and mold growth.

    One of the most important tasks is cleaning the toilet regularly using disinfectant cleaners. The toilet seat, handle, and surrounding areas should be wiped frequently to prevent germ buildup. Using disposable gloves during this process ensures better hygiene.

    Sinks and countertops also require daily attention. Toothpaste residue, soap scum, and water spots can accumulate quickly. Wiping these surfaces with a disinfectant cloth keeps them clean and visually appealing.

    Another critical area is the shower and tiles. Mold can develop in grout lines if moisture remains for long periods. Scrubbing tiles with a mild cleaning solution and ensuring proper ventilation helps prevent mold formation.

    Finally, bathroom floors should be mopped regularly to remove dirt and bacteria tracked in from other parts of the home. Keeping cleaning tools specifically for the bathroom prevents cross-contamination.

    By following these simple cleaning practices, maintaining a fresh and germ-free bathroom becomes much easier.
    """
  },

  {
    "id":6,
    "title": "Eco Friendly Cleaning Solutions for a Healthier Home",
    "image_url": "https://images.unsplash.com/photo-1527515637462-cff94eecc1ac",
    "author": "Sneha Patel",
    "date_of_written": "2026-02-01",
    "read_time": "4 min",
    "category": "tips and tricks",
    "tags": ["eco cleaning","natural cleaners","green cleaning"],
    "content": """
    Eco-friendly cleaning is becoming increasingly popular as more people seek safer alternatives to chemical-based products. Natural cleaning solutions can effectively remove dirt and bacteria while reducing environmental impact.

    One of the most versatile natural cleaners is vinegar. Mixed with water, it can be used to clean glass, countertops, and kitchen surfaces. Its mild acidity helps dissolve grease and mineral deposits.

    Baking soda is another powerful natural cleaner. It works well for removing stains, deodorizing carpets, and scrubbing sinks or stovetops. Because it is non-toxic, it is safe to use around children and pets.

    Lemon juice is also commonly used in natural cleaning solutions. Its antibacterial properties make it effective for cutting grease and eliminating odors in kitchens and refrigerators.

    Using reusable cloths instead of disposable wipes further reduces waste. Many households are switching to refillable spray bottles and homemade cleaning mixtures to reduce plastic usage.

    Adopting eco-friendly cleaning methods not only benefits the environment but also creates a healthier indoor space with fewer harsh chemicals.
    """
  },

  {
    "id":7,
    "title": "Daily Cleaning Habits That Save Time",
    "image_url": "https://images.unsplash.com/photo-1603712725038-e9334ae8f39f",
    "author": "Amit Kulkarni",
    "date_of_written": "2026-02-05",
    "read_time": "3 min",
    "category": "tips and tricks",
    "tags": ["daily cleaning","quick cleaning","cleaning routine"],
    "content": """
    Many people think cleaning requires long hours of work, but simple daily habits can keep a home tidy without overwhelming effort. Consistency is the key to maintaining cleanliness.

    One helpful habit is making the bed every morning. This small task instantly improves the appearance of a bedroom and sets a positive tone for the day. It also prevents clutter from accumulating.

    Another useful routine is wiping kitchen surfaces after each meal. Food spills and crumbs can attract insects and bacteria if left unattended. A quick wipe keeps the kitchen hygienic.

    Laundry is another area where small actions make a difference. Doing smaller loads regularly prevents large piles from building up and keeps clothes organized.

    Taking a few minutes each evening to tidy living spaces can also help maintain cleanliness. Returning items to their proper places prevents clutter and makes the home more comfortable.

    Over time, these simple habits become part of everyday life, making cleaning less stressful and more manageable.
    """
  },

  {
    "id":8,
    "title": "Smart Cleaning Gadgets Transforming Home Hygiene",
    "image_url": "https://images.unsplash.com/photo-1581579188871-45ea61f2a1c8",
    "author": "Karan Malhotra",
    "date_of_written": "2026-02-12",
    "read_time": "4 min",
    "category": "innovation",
    "tags": ["smart cleaning","cleaning gadgets","home technology"],
    "content": """
    Technology is rapidly transforming the way people clean their homes. Smart cleaning gadgets are designed to save time while improving hygiene and convenience.

    Robot vacuum cleaners are among the most popular innovations. These devices automatically navigate rooms, removing dust and debris from floors without manual effort. Many models can be controlled through mobile apps and scheduled to clean at specific times.

    Another innovative device is the UV sanitizing cleaner. These tools use ultraviolet light to eliminate bacteria on surfaces such as phones, keyboards, and countertops. They provide an additional layer of hygiene beyond traditional cleaning.

    Steam cleaning machines are also gaining popularity. By using high-temperature steam, they can remove dirt, grease, and germs without chemical cleaning agents. This makes them a safer option for households with children or pets.

    Smart cleaning tools not only improve efficiency but also encourage consistent cleaning routines. As technology continues to evolve, these devices will play an increasingly important role in maintaining healthy and hygienic homes.
    """
  },

  {
    "id":9,
    "title": "How to Maintain Clean Floors Easily",
    "image_url": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a",
    "author": "Deepika Singh",
    "date_of_written": "2026-02-18",
    "read_time": "3 min",
    "category": "cleaning techniques",
    "tags": ["floor cleaning","mopping","home hygiene"],
    "content": """
    Floors collect dust, dirt, and bacteria every day, making them an important part of household cleaning routines. Keeping floors clean not only improves appearance but also contributes to overall hygiene.

    Sweeping or vacuuming floors daily helps remove loose dust and debris. This prevents particles from spreading to other areas of the home. Vacuum cleaners with strong suction are especially effective for carpets and rugs.

    Mopping is another essential step. Using warm water with a gentle floor cleaner helps remove stains and bacteria. Microfiber mops are recommended because they capture dirt more efficiently and require less water.

    Placing doormats at entrances can also reduce the amount of dirt brought into the house. Encouraging family members to remove shoes indoors further keeps floors cleaner.

    Regular floor cleaning not only improves hygiene but also extends the lifespan of flooring materials, keeping them looking new for longer.
    """
  },

  {
    "id":10,
    "title": "Professional Cleaning Techniques Used by Experts",
    "image_url": "https://images.unsplash.com/photo-1585421514284-efb74c2b69ba",
    "author": "Vikram Shah",
    "date_of_written": "2026-02-25",
    "read_time": "5 min",
    "category": "cleaning techniques",
    "tags": ["professional cleaning","deep cleaning","cleaning methods"],
    "content": """
    Professional cleaners follow specific techniques that allow them to clean efficiently while achieving excellent results. Understanding these methods can help homeowners improve their own cleaning routines.

    One important technique is cleaning from top to bottom. Professionals start with higher surfaces such as shelves and cabinets before moving to floors. This ensures that dust falling from upper areas is cleaned during the final steps.

    Another common strategy is using color-coded cleaning cloths. Different colored cloths are used for specific areas like kitchens, bathrooms, and general surfaces. This prevents cross-contamination between spaces.

    Professionals also rely on the correct cleaning solutions for different surfaces. Using the right product helps remove stains effectively without damaging materials like wood, glass, or stone.

    Time management is another key factor. Cleaning experts often divide spaces into zones and focus on one section at a time, ensuring thorough coverage without missing areas.

    By adopting these professional techniques, homeowners can make their cleaning routines more organized and efficient while maintaining a higher standard of hygiene.
    """
  }
]

#creating home, about, register page
@csrf_exempt
def home(request):
    # return render(request, 'home.html')
    if request.method=="POST":
        email=request.POST.get("loginEmail").strip()
        password=request.POST.get("loginPassword").strip()
        remember=request.POST.get("loginRemember")
        

        if (email=="" or password==""):
            return render(request, "home.html", {"message":"email and password is required", "open_login":True, "cleaningService":CleaningServices})
        else:
            customer=Customer.objects.filter(email=email).first()
            if (customer and check_password(password, customer.password)):
                
                #Creating session with id
                request.session['user_id']=str(customer.id)
                request.session['user_email']=customer.email
                request.session['user_name']=customer.username

                if remember == "on":
                    request.session.set_expiry(10000) #session expired in 2 min= 2*60=120
                else:
                    request.session.set_expiry(3000) #session expired in 2 min= 2*60=120

                return render(request,"home.html", {"currentUser":request.session.get('user_name', ""), "cleaningService":CleaningServices})
            else:
                return render(request, "home.html", {"currentUser":request.session.get('user_name', ""),"message":"Invalid email or password. Please try again.", "open_login":True, "cleaningService":CleaningServices})
    else:
        return render(request, "home.html",{"currentUser":request.session.get('user_name', ""),"cleaningService":CleaningServices})
    

def bookService(request, serviceId,):
    # currentUser=request.user if request.user.is_authenticated else None
    # if(currentUser):
    for key, value in CleaningServices.items():
        for cs in value:
            if(cs["id"]==serviceId):
                return render(request, "bookService.html", {"userService":cs, "currentUser":request.session.get('user_name', ""), "CleaningServices":CleaningServices})
    
    return redirect('home')




def services(request):
    return render(request, 'services.html', {"services":CleaningServices,"currentUser":request.session.get('user_name', "")})

def pricing(request):
    return render(request, "pricing.html", {"services":CleaningServices,"PricingPlan":PricingPlan,"currentUser":request.session.get('user_name', "")})

def blog(request):
    CustomerBlog=CleanzaBlog.objects.all()
    if request.session.get('user_id'):
      myblog=CleanzaBlog.objects.filter(publisher=request.session.get('user_id',""))
      return render(request, 'blog.html', {"myBlog":myblog,"CustomerBlog":CustomerBlog,"blogData":blogData,"services":CleaningServices,"currentUser":request.session.get('user_name', "")})
    return render(request, 'blog.html', {"CustomerBlog":CustomerBlog,"blogData":blogData,"services":CleaningServices,"currentUser":request.session.get('user_name', "")})

def write_blog(request):
    CustomerBlog=CleanzaBlog.objects.all()
    if not request.session.get('user_id'):
      return render(request, "blog.html", {"CustomerBlog":CustomerBlog,"blogData":blogData,"services":CleaningServices,"message":"Please Login to Write & Access Your Blog", "open_login":True, "cleaningService":CleaningServices})
    currentCustomer=Customer.objects.get(id=request.session.get("user_id",""))
    return render(request,'writeBlog.html', {"currentCustomer":currentCustomer, "currentUser":request.session.get('user_name', "")})

@csrf_exempt
def blog_submission(request):
    if not request.session.get('user_id'):
        return render(request, "blog.html", {"blogData":blogData,"services":CleaningServices,"message":"Please Login to Write & Access Your Blog", "open_login":True, "cleaningService":CleaningServices})
    if request.method=="POST":
        try:
            webBlogData=json.loads(request.body)
            blogTitle=webBlogData.get('blogTitle')
            blogThumbnail=webBlogData.get('blogThumbnail')
            content=webBlogData.get('content')
            blogCatgory=webBlogData.get('blogCatgory')
            readTime=int(webBlogData.get('readTime'))
            currentDate=date.today()
            currentCustomer=Customer.objects.get(id=request.session.get('user_id', ""))
            saveBlog=CleanzaBlog.objects.create(publisher=currentCustomer, title=blogTitle, thumbnail=blogThumbnail,content=content, dateOfPublish=currentDate, category=blogCatgory, readTime=readTime)
            saveBlog.save()
            messages.success(request,"Blog has been published successfully.")
            return redirect("blog")
        except Exception as e:
            print(e)


def read_blog(request, blogId):
    if not request.session.get("user_id"):
        CustomerBlog=CleanzaBlog.objects.all()
        return render(request, "blog.html", {"CustomerBlog":CustomerBlog,"blogData":blogData,"services":CleaningServices,"message":"Please Login to Write & Access Your Blog", "open_login":True, "cleaningService":CleaningServices})
    currentCustomer = Customer.objects.get(id=request.session.get("user_id",""))
    customerBlog = CleanzaBlog.objects.filter(id=int(blogId))

    for blog in blogData:
        if blog['id'] == int(blogId):
            if customerBlog:
                return render(request, "ReadBlog.html", {
                    "customerBlog": customerBlog,
                    "currentCustomer": currentCustomer,
                    "currentReadBlog": blog
                })
            else:
                return render(request, "ReadBlog.html", {
                    "currentCustomer": currentCustomer,
                    "currentReadBlog": blog
                })

    return render(request, "ReadBlog.html", {"currentCustomer":currentCustomer, "currentUser":request.session.get('user_name', "")})



def project(request):
    return render(request, 'project.html',{"services":CleaningServices,"currentUser":request.session.get('user_name', "")})

def contact(request):
    if request.method=="POST":
        ContactName=request.POST.get('ContactName').strip()
        ContactEmail=request.POST.get('ContactEmail').strip()
        ContactPhone=request.POST.get('ContactPhone').strip()
        ContactService=request.POST.get('ContactService').strip()
        ContactMessage=request.POST.get('ContactMessage').strip()
        if(ContactName=="" or ContactEmail=="" or ContactService=="" or len(ContactMessage)<=5 or ContactPhone==""):
            messages.error(request,"Please fill each and every details properly")
            return redirect("contact")
        else:
          if(ContactUs.objects.filter(ContactEmail=ContactEmail).exists()):
            messages.error(request,"You might have already reached out to us—we appreciate it.")
            return redirect("contact")
          else:
            ContactUs.objects.create(ContactName=ContactName, ContactEmail=ContactEmail, ContactPhone=ContactPhone, ContactQuery=ContactService, ContactMessage=ContactMessage)
            messages.success(request,"Thank you for contact us, We approach you as soon as possible.")
            return redirect("contact")
            
        # messages.success("Thank you for contact us, We approach you as soon as possible.")
    if not request.session.get('user_id'):
        return render(request, 'contact.html', {"services":CleaningServices,"currentUser":request.session.get('user_name', "")})
    currentCustomer=Customer.objects.get(id=request.session.get('user_id',""))
    return render(request, 'contact.html', {"currentCustomer":currentCustomer,"services":CleaningServices,"currentUser":request.session.get('user_name', "")})

# Search box 
def search(request):
    return render(request, 'SearchBox.html', {"blogData":blogData,"services":CleaningServices,"currentUser":request.session.get('user_name', "")})

def register(request):
    # return render(request,"register.html")
    if request.method=="POST":
        name=request.POST.get("name","").strip()
        username=request.POST.get("username","").strip()
        phone=request.POST.get("phone","").strip()
        email=request.POST.get("email","").strip()
        address=request.POST.get("address","").strip()
        city=request.POST.get("city","").strip()
        state=request.POST.get("state","").strip()
        areaCode=request.POST.get("areaCode","").strip()
        country=request.POST.get("country","").strip()
        gender=request.POST.get("gender","").strip()
        password=request.POST.get("password","").strip()
        confirmPassword=request.POST.get("confirmPassword","").strip()
        remember=request.POST.get("remember")
        if(name=="" or username=="" or phone=="" or email=="" or address=="" or city=="" or state=="" or areaCode=="" or country=="" or gender=="" or password=="" or confirmPassword==""):
          return render(request, "register.html", {"error":"All fields in the form must be completed correctly before submission."})
        else:  
          if(password!=confirmPassword):
              return render(request, "register.html", {"error":"Password should be same"})

          if(Customer.objects.filter(username=username).exists()):
              return render(request, "register.html", {"error":"Username is already exists"})

          if(Customer.objects.filter(email=email).exists()):
              return render(request, "register.html", {"error":"email is already exists"})

          try:
              customer= Customer(name=name,username=username,phone=phone,email=email.lower(),address=address,city=city,state=state,areaCode=areaCode,country=country,gender=gender,password=make_password(password),remember=True if remember=="on" else False,time=datetime.today())
              customer.save()
              return render(request, "register.html", {"error":"Registration Successful", "open_login":True})
          except Exception as e:
             return render(request, "register.html", {"error":"Registration Failed"})
    else:
        return render(request, "register.html")
   

def ScheduleService(request, serviceId):
    if not request.session.get('user_id'):
      return render(request, "home.html", {"message":"Login to Book Schedule", "open_login":True, "cleaningService":CleaningServices})
    
    for key,value in CleaningServices.items():
        for ServiceForBooking in value:
            if (ServiceForBooking["id"]==serviceId):
                
                currentCustomer=Customer.objects.get(id=request.session.get('user_id',""))
                return render(request, "ScheduleService.html", {"ServiceForBooking":ServiceForBooking,"currentCustomer":currentCustomer,"currentUser":request.session.get('user_name', ""), "CurrentUserEmail":request.session.get('user_email', "")})

@csrf_exempt
def service_booking_submission(request):
    if request.method=="POST":
        try:
            webpageData=json.loads(request.body)
            customer_id=webpageData.get("Customer")
            customer=Customer.objects.get(id=customer_id)
            service_name=webpageData.get("service_name")
            time=webpageData.get("time") 
            date_str = webpageData.get("date")  # "Mon Feb 21 2026"
            date = datetime.strptime(date_str, "%a %b %d %Y").date() 
            Service_Address =webpageData.get("Service_Address") 
            TotalCharge =str(webpageData.get("TotalCharge") or "0")
            Customer_Instruction =webpageData.get("Customer_Instruction")
            Booking_DateTime =webpageData.get("Booking_DateTime")

            mybooking=Booking.objects.create(Customer=customer, Service_name=service_name,time=time,date=date,Service_Address=Service_Address,Customer_Instruction=Customer_Instruction,TotalCharge=TotalCharge,Booking_DateTime=Booking_DateTime)

            if (service_name=="Deep Home Cleaning" or service_name=="Basic Home Cleaning"):
                propertyType=webpageData.get("propertyType")
                No_Of_Bedroom =int(webpageData.get("No_Of_Bedroom") or 0)
                No_Of_Bathroom =int(webpageData.get("No_Of_Bathroom") or 0)
                Is_UV_Sanitization =webpageData.get("Is_UV_Sanitization")
                ResidentalCleaning.objects.create(HomeBooking=mybooking, propertyType=propertyType,No_Of_Bedroom=No_Of_Bedroom,No_Of_Bathroom=No_Of_Bathroom,Is_UV_Sanitization=Is_UV_Sanitization)
            elif(service_name=="Kitchen Deep Cleaning"):
                KitchenType=webpageData.get("KitchenType")
                GreaseLevel=webpageData.get("GreaseLevel")
                Is_Chimney_Cleaning=webpageData.get("Is_Chimney_Cleaning")
                KitchenCleaning.objects.create(KitchenBooking=mybooking,KitchenType=KitchenType,GreaseLevel=GreaseLevel,Is_Chimney_Cleaning=Is_Chimney_Cleaning)
            elif(service_name=="Bathroom and Toilet Cleaning"):
                BathroomType=webpageData.get("BathroomType")
                No_Of_Toilet=int(webpageData.get("No_Of_Toilet") or 0)
                No_Of_Bathroom=int(webpageData.get("No_Of_Bathroom") or 0)
                Is_Hardwater_Stain=webpageData.get("Is_Hardwater_Stain")
                BathroomCleaning.objects.create(BathroomBooking=mybooking,BathroomType=BathroomType,No_Of_Toilet=No_Of_Toilet,No_Of_Bathroom=No_Of_Bathroom,Is_Hardwater_Stain=Is_Hardwater_Stain)
            elif(service_name=="Office Cleaning" or service_name=="Office Deep Cleaning"):
                OfficeSize=webpageData.get("OfficeSize")
                No_Of_Washroom=int(webpageData.get("No_Of_Washroom") or 0)
                Is_Glass_Partition=webpageData.get("Is_Glass_Partition")
                Is_UV_Sanitization=webpageData.get("Is_UV_Sanitization")
                OfficeCleaning.objects.create(OfficeBooking=mybooking,OfficeSize=OfficeSize,No_Of_Washroom=No_Of_Washroom,Is_Glass_Partition=Is_Glass_Partition,Is_UV_Sanitization=Is_UV_Sanitization)
            elif(service_name=="Garden Cleaning"):
                GardenSize=webpageData.get("GardenSize")
                Is_Grass_Trimming=webpageData.get("Is_Grass_Trimming")
                Is_Tree_Trimming=webpageData.get("Is_Tree_Trimming")
                GardenCleaning.objects.create(GardenBooking=mybooking,GardenSize=GardenSize,Is_Grass_Trimming=Is_Grass_Trimming,Is_Tree_Trimming=Is_Tree_Trimming)
            elif(service_name=="Tree Cutting and Trimming"):
                Tree_Service_Type=webpageData.get("Tree_Service_Type")
                No_Of_Tree=int(webpageData.get("No_of_Tree") or 0)
                Tree_Max_Height=webpageData.get("Tree_Max_Height")
                TreeCleaning.objects.create(TreeBooking=mybooking,Tree_Service_Type=Tree_Service_Type,No_Of_Tree=No_Of_Tree,Tree_Max_Height=Tree_Max_Height)
            elif(service_name=="Sofa and Carpet Cleaning"):
                SofaType=webpageData.get("SofaType")
                No_Of_Seat=int(webpageData.get("No_of_Seat") or 0)
                Is_Stain_Cleaning=webpageData.get("Is_Stain_Cleaning")
                SofaCleaning.objects.create(SofaBooking=mybooking,SofaType=SofaType,No_Of_Seat=No_Of_Seat,Is_Stain_Cleaning=Is_Stain_Cleaning)
            elif(service_name=="Window and Glass Cleaning"):
                WindowType=webpageData.get("WindowType")
                No_Of_Window=int(webpageData.get("No_of_Window") or 0)
                Window_Side=webpageData.get("Window_Side")
                Window_Height=webpageData.get("Window_Height")
                WindowCleaning.objects.create(WindowBooking=mybooking,WindowType=WindowType,No_Of_Window=No_Of_Window,Window_Side=Window_Side,Window_Height=Window_Height)
            elif(service_name=="Post-Construction Cleaning"):
                ConstructionType=webpageData.get("ConstructionType")
                PropertySize=webpageData.get("PropertySize")
                Is_Construction_Stain=webpageData.get("Is_Construction_Stain")
                Post_ConstructionCleaning.objects.create(ConstructionBooking=mybooking,ConstructionType=ConstructionType,PropertySize=PropertySize,Is_Construction_Stain=Is_Construction_Stain)


            return JsonResponse({"status": "success",})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
        
    return JsonResponse({"status": "fail"}, status=400)

# CUSTOMER DASHBOARD
def dashboard(request):
    if not request.session.get('user_id'): #agar session nahi mila toh
      return render(request, "home.html", {"message":"Please Login to Access Dashboard", "open_login":True, "cleaningService":CleaningServices})
    
    #agar session mila toh
    UserBookingList=Booking.objects.filter(Customer=request.session.get("user_id"))
    ResidentalBookingList=ResidentalCleaning.objects.filter(HomeBooking__Customer=request.session.get("user_id",""))
    currentCustomer=Customer.objects.get(id=request.session.get('user_id',""))
    contextData={
        "UserBookingList":UserBookingList,
        "ResidentalBookingList":ResidentalBookingList,
        "currentCustomer":currentCustomer,
        "currentUser":request.session.get('user_name', ""),
        "CurrentUserEmail":request.session.get('user_email', "")
    }
    return render(request, 'dashboard.html', contextData)


#Deletion of booked service
def service_booking_delete(request, serviceDeleteId):
    bookedService=Booking.objects.get(id=serviceDeleteId)
    bookedService.delete()
    messages.success(request,"Booking has been deleted successfully.")
    return redirect('dashboard')

#reschedule booking
def service_booking_reschedule(request, bookedServiceId):
    if not request.session.get('user_id'): #agar session nahi mila toh
      return render(request, "home.html", {"message":"Please Login to Manage Booking", "open_login":True, "cleaningService":CleaningServices})
    
    try:
      bookedService=Booking.objects.get(id=bookedServiceId)
      bookedService=Booking.objects.get(id=bookedServiceId)
      serviceName=bookedService.Service_name
      checkServiceForReview=Booking.objects.filter(Customer=request.session.get("user_id"), Service_name=serviceName)
      if(checkServiceForReview):
        return render(request, 'RescheduleBooking.html', {"bookedService":bookedService,"services":CleaningServices,"currentUser":request.session.get('user_name', "")})
    except Exception as e:
        messages.error(request, "Service is not exists")
        return redirect('dashboard')
        

@csrf_exempt
def booking_Reschedule_Submission(request):
    if not request.session.get('user_id'): #agar session nahi mila toh
      return render(request, "home.html", {"message":"Please Login to Manage Booking", "open_login":True, "cleaningService":CleaningServices})
    
    if(request.method=="POST"):
        rescheduleWebData=json.loads(request.body)
        RescheduleService=rescheduleWebData.get("RescheduleService")
        RescheduleDate=rescheduleWebData.get("RescheduledDate")
        RescheduledTime=rescheduleWebData.get("RescheduledTime")

        Booking.objects.filter(Customer=request.session.get("user_id"), Service_name=RescheduleService).update(date=RescheduleDate, time=RescheduledTime)
        messages.success(request,"Booking has been reschedule successfully.")
        return redirect('dashboard')
         
    
#Booking Review
def service_booking_review(request, bookedServiceReview):
    if not request.session.get('user_id'): #agar session nahi mila toh
      return render(request, "home.html", {"message":"Please Login to Write Review", "open_login":True, "cleaningService":CleaningServices})
    # bookedService=Booking.objects.get(id=bookedServiceReview)
    try:
        bookedService=Booking.objects.get(id=bookedServiceReview)
        serviceName=bookedService.Service_name
        checkServiceForReview=Booking.objects.filter(Customer=request.session.get("user_id"), Service_name=serviceName)
        if(checkServiceForReview):
            return render(request, 'ReviewBooking.html', {"bookedService":bookedService,"services":CleaningServices,"currentUser":request.session.get('user_name', "")})
        else:
            messages.error(request, "Service is not booked")
            return redirect('dashboard')
    except Exception as e:
        messages.error(request, "Service is not booked")
        return redirect('dashboard')

@csrf_exempt   
def booking_Review_Submission(request):
    if(request.method=="POST"):
        try:
            reviewWebData=json.loads(request.body)
            #webpage data
            CurrentCustomer=Customer.objects.get(id=request.session.get("user_id", ))
            ReviewService=Booking.objects.get(id=reviewWebData.get("ReviewServiceId"))
            ReviewRating=int(reviewWebData.get("ReviewRating"))
            ReviewText=reviewWebData.get("ReviewText")

            FeedbackWrite=CustomerFeedback.objects.create(Reviewer=CurrentCustomer,ReviewBooking=ReviewService,ReviewRating=ReviewRating,ReviewText=ReviewText)
            FeedbackWrite.save()
            messages.success(request,"Booking has been reschedule successfully.")
            return redirect('dashboard')
        except Exception as e:
            print(e)


#Community Support
def community_support(request):
    if(request.method == "POST"):
        CommunityWebData=json.loads(request.body)
        CommunityEmail=CommunityWebData.get('CommunityEmail')
        if not CleanzaCommunity.objects.filter(CommunityEmail=CommunityEmail).exists():
            CommunityDataCollection=CleanzaCommunity.objects.create(CommunityEmail=CommunityEmail)
            CommunityDataCollection.save()
            return render(request, 'NavbarModel.html', {"services":CleaningServices,"currentUser":request.session.get('user_name', "")})
            


#When logout
def logout(request):
    request.session.flush() #completely destroy session
    return render(request, "home.html", {"message":"You're logged out", "open_login":True, "cleaningService":CleaningServices})

#User Account
def myAccount(request):
    if not request.session.get('user_id'):
      return render(request, "home.html", {"message":"Login to Access Your Account", "open_login":True, "cleaningService":CleaningServices})
    currentCustomer=Customer.objects.get(id=request.session.get('user_id',""))
    return render(request, 'MyAccount.html', {"currentCustomer":currentCustomer,"services":CleaningServices,"currentUser":request.session.get('user_name', "")})

def update_profile(request):
    if not request.session.get('user_id'):
      return render(request, "home.html", {"message":"Login to Access Your Account", "open_login":True, "cleaningService":CleaningServices})
    if request.method=="POST":
        profileWebData=json.loads(request.body)
        UserName=profileWebData.get('UserName')
        UserFullName=profileWebData.get('UserFullName')
        UserGender=profileWebData.get('UserGender')
        UserBio=profileWebData.get('UserBio')
        Customer.objects.filter(id=request.session.get('user_id'), email=request.session.get('user_email')).update(username=UserName, name=UserFullName,gender=UserGender,bio=UserBio)
        return redirect('myAccount')
    
def update_contact(request):
    if not request.session.get('user_id'):
      return render(request, "home.html", {"message":"Login to Access Your Account", "open_login":True, "cleaningService":CleaningServices})
    if request.method=="POST":
        contactWebData=json.loads(request.body)
        UserPhone=contactWebData.get('UserPhone')
        Customer.objects.filter(id=request.session.get('user_id'), email=request.session.get('user_email')).update(phone=UserPhone)
        return redirect('myAccount')
    
def update_address(request):
    if not request.session.get('user_id'):
      return render(request, "home.html", {"message":"Login to Access Your Account", "open_login":True, "cleaningService":CleaningServices})
    if request.method=="POST":
        addressWebData=json.loads(request.body)
        UserAddress=addressWebData.get('UserAddress')
        UserCity=addressWebData.get('UserCity')
        UserState=addressWebData.get('UserState')
        UserAreaCode=addressWebData.get('UserAreaCode')
        UserCountry=addressWebData.get('UserCountry')
        Customer.objects.filter(id=request.session.get('user_id'), email=request.session.get('user_email')).update(address=UserAddress,city=UserCity,state=UserState,areaCode=UserAreaCode,country=UserCountry)
        return redirect('myAccount')
    
def update_password(request):
    if not request.session.get('user_id'):
      return render(request, "home.html", {"message":"Login to Access Your Account", "open_login":True, "cleaningService":CleaningServices})
    if request.method=="POST":
        passwordWebData=json.loads(request.body)
        UserCurrentPassword=passwordWebData.get('UserCurrentPassword')
        UserNewPassword=passwordWebData.get('UserNewPassword')
        UserConfirmPassword=passwordWebData.get('UserConfirmPassword')
        
        currentUser=Customer.objects.get(id=request.session.get('user_id'))
        if check_password(UserCurrentPassword, currentUser.password):
            currentUser.password=make_password(UserNewPassword)
            currentUser.save()
            return redirect('myAccount')
        # else:
        #     print("Password is invalid")
        # Customer.objects.filter(id=request.session.get('user_id'), password=make_password(UserCurrentPassword)).update(password=make_password(UserNewPassword))
        # return redirect('myAccount')
    

#User Settings
def mySetting(request):
    if not request.session.get('user_id'):
      return render(request, "home.html", {"message":"Login to Access Your Account & Settings", "open_login":True, "cleaningService":CleaningServices})
    currentCustomer=Customer.objects.get(id=request.session.get('user_id',""))
    isSettingUserExists=UserSetting.objects.filter(User=currentCustomer)
    if(isSettingUserExists):
      userSetting=UserSetting.objects.get(User=currentCustomer)
      return render(request, 'MySetting.html', {"userSetting":userSetting,"currentCustomer":currentCustomer,"services":CleaningServices,"currentUser":request.session.get('user_name', "")})
    else:  
      return render(request, 'MySetting.html', {"currentCustomer":currentCustomer,"services":CleaningServices,"currentUser":request.session.get('user_name', "")})

def change_Setting(request):
    if not request.session.get('user_id'):
      return render(request, "home.html", {"message":"Login to Access Your Account & Settings", "open_login":True, "cleaningService":CleaningServices})
    if request.method=="POST":
        settingWebData=json.loads(request.body)
        UserTheme=settingWebData.get('UserTheme')
        UserFontSize=settingWebData.get('UserFontSize')
        UserEmailNotification=settingWebData.get('UserEmailNotification')
        UserWebNotification=settingWebData.get('UserWebNotification')
        UserLanguage=settingWebData.get('UserLanguage')
        UserTimeZone=settingWebData.get('UserTimeZone')
        currentCustomer=Customer.objects.get(id=request.session.get('user_id',""))
        isSettingUserExists=UserSetting.objects.filter(User=currentCustomer)
        if(isSettingUserExists):
            UserSetting.objects.filter(User=currentCustomer).update(WebTheme=UserTheme,WebFontSize=UserFontSize,IsEmailNotification=UserEmailNotification, IsWebNotification=UserWebNotification, WebLanguage=UserLanguage, WebTimeZone=UserTimeZone)
        else:  
          UserSetting.objects.create(User=currentCustomer, WebTheme=UserTheme,WebFontSize=UserFontSize,IsEmailNotification=UserEmailNotification, IsWebNotification=UserWebNotification, WebLanguage=UserLanguage, WebTimeZone=UserTimeZone)
    return redirect('mySetting')

#User Help & support
def faqSupport(request):
    return render(request, 'FaqSupport.html', {"services":CleaningServices,"currentUser":request.session.get('user_name', "")})

#email verification
def generatOtp():
    randomEmailCode=random.randint(100001,999999)
    return randomEmailCode

def email_verification(request):
    if not request.session.get('user_id'):
      return render(request, "home.html", {"message":"Login to Access Your Account & Settings", "open_login":True, "cleaningService":CleaningServices})
    currentCustomer=Customer.objects.get(id=request.session.get('user_id'))

    if currentCustomer.isEmailVerified!='Verified':
        randomEmailCode=generatOtp()
        request.session["email_otp"]=randomEmailCode
        #sending email using SendMail function module
        subject = "Your Email Verification OTP"
        message = f"""
        Hello,
        Thank you for registering.

        Your One-Time Password (OTP) for email verification is:
        OTP: {randomEmailCode}

        This OTP is valid for the next 10 minutes. Please do not share this code with anyone.
        If you did not request this verification, please ignore this email.

        Best regards,
        Cleanify Application Team
        """
        receiverEmail=currentCustomer.email
        try:
          send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[receiverEmail],
            fail_silently=False
          )
          return render(request, "EmailVerification.html",{"currentCustomer":currentCustomer,"services":CleaningServices,"currentUser":request.session.get('user_name', "")})
        except Exception as e:
            print("EMAIL ERROR:", e)
            messages.error(request, "Unable to send verification email. Please try again later.")
            return redirect('myAccount')
    else:
        messages.error(request, "You are email is already verified")
        return redirect('myAccount')


#check email verification code validity
def emailVerifiedCodeCheck(request):
    if not request.session.get('user_id'):
      return render(request, "home.html", {"message":"Login to Access Your Account & Settings", "open_login":True, "cleaningService":CleaningServices})
    currentCustomer=Customer.objects.get(id=request.session.get('user_id'))
    if request.method=="POST":
      emailWebData=json.loads(request.body)
      emailCode=int(emailWebData.get('inputCode') or 0)
      if(emailCode==int(request.session.get('email_otp'))):
          currentCustomer.isEmailVerified='Verified'
          currentCustomer.save()
          return redirect('dashboard')
      else:
          return redirect('emailVerifiedCodeCheck')
    return redirect('dashboard')

#page not found 404/500
def pageNotFound(request, exception):
    return render(request, 'PageNotFound404.html', {"services":CleaningServices,"currentUser":request.session.get('user_name', "")}, status=404)

def pageNotFound505(request):
    return render(request, 'PageNotFound404.html', {"services":CleaningServices,"currentUser":request.session.get('user_name', "")}, status=404)


