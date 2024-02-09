# Diccionario de datos: 


>  Google Maps
 

* ***Metadata*** es un dataset que contiene información de comercios de Estados Unidos, incluyendo localización, atributos y categorías. Las variables que contiene son:  

    * **Name**: 'Walgreens Pharmacy'.
    
    * **Category**: 'Pharmacy'.
    * **Location**: '41.451859999999996 , -85.2666757'.
    * **Dirección**: '124 E North St'.
    * **Ciudad**: 'Kendallville'.
    * **Estado**: 'Indiana'.
    * **codigo_postal**: 950012.
    
    

* ***review-estados*** es un dataset que contiene información de las reviews de los usuarios. Las variables que contiene son: 

    * **User_id**: '101463350189962023774'.
    * **nombre**: 'Jordan Adams'.
    * **Rating**: 5.
    * **Text**: 'Cool place, great people, awesome dentist!'.
    * **Resp**: 'True.
    * **gmap_id**: '1564844651654.
    * **Sentimiento**:  Define umbrales para clasificar las reseñas en positivas, neutrales y negativas
    * **Sentiment_analysis**: 0 si es negativo, 1 si es neutro, 2 si es positivo.

>  Yelp


* ***business.pkl*** es un dataset que contiene información del comercio, incluyendo localización, atributos y categorías. Las variables que contiene son:  

    * **Business_id**: 'tnhfDv5Il8EaGSXZGiuQGg'.
    * **Name**: 'Garaje'.
    * **Address**: '475 3rd St'.
    * **City**: 'San Francisco'.
    * **State**: 'CA'.
    * **Latitude**: 37.7817529521.
    * **Longitude**: -122.39612197.
    * **Stars**:  4.5.
    * **Review_count**: 1198.
    * **Is_open**: 0 si esta cerrado, 1 si está abierto.
    * **Categories**: 'Burger'.
    * **Location**: '37.7817529521 , -122.39612197'.

* ***review.json*** es un dataset que contiene las reseñas completas, incluyendo el user_id que escribió el review y el business_id por el cual se escribe la reseña. Las variables que contiene son:  

    * **Business_id**: 'tnhfDv5Il8EaGSXZGiuQGg'.
    * **User_id**: 'Ha3iJu77CxlrFm-vQRs_8g'.
    * **Stars**: 4.
    * **Date**: '2016-03-09'.
    * **Text**: 'Great place to hang out after work: the prices are decent, and the ambience is fun. It's a bit loud, but very lively. The staff is friendly, and the food is good. They have a good selection of drinks.'.
    * **Sentimiento**:  Define umbrales para clasificar las reseñas en positivas, neutrales y negativas
    * **Sentiment_analysis**: 0 si es negativo, 1 si es neutro, 2 si es positivo.

* ***checkin.json*** es un dataset que contiene las reseñas completas, incluyendo el user_id que escribió el review y el business_id por el cual se escribe la reseña. Las variables que contiene son:  

    * **Business_id**: 'tnhfDv5Il8EaGSXZGiuQGg'.
    * **Date**: '2016-04-26'.