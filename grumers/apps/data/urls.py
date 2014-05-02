from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    'grumers.apps.data.views',
    url(r'^observation/create/?$',
        views.JellyfishObservationCreate.as_view(),
        name='data_observation_create',
        ),
    url(r'^observation/(?P<pk>\d+)/update/?$',
        views.JellyfishObservationUpdate.as_view(),
        name='data_observation_update',
        ),
    url(r'^observation/(?P<pk>\d+)/delete/?$',
        views.JellyfishObservationDelete.as_view(),
        name='data_observation_delete',
        ),
    url(r'^observation/list/?$',
        views.JellyfishObservationList.as_view(),
        name='data_observation_list',
        ),
    url(r'^observation/heatmap/?$',
        views.JellyfishObservationHeatmap.as_view(),
        name='data_observation_heatmap',
        ),
    url(r'^route/(?P<pk_route>\d+)/observation/create/?$',
        views.JellyfishObservationCreate.as_view(),
        name='data_route_observation_create',
        ),
    url(r'^route/(?P<pk_route>\d+)/observation/(?P<pk>\d+)/update/?$',
        views.JellyfishObservationUpdate.as_view(),
        name='data_route_observation_update',
        ),
    url(r'^route/(?P<pk_route>\d+)/observation/(?P<pk>\d+)/delete/?$',
        views.JellyfishObservationDelete.as_view(),
        name='data_route_observation_delete',
        ),
    url(r'^route/(?P<pk_route>\d+)/observation/list/?$',
        views.JellyfishObservationList.as_view(),
        name='data_route_observation_list',
        ),
    url(r'^route/(?P<pk_route>\d+)/observation/heatmap/?$',
        views.JellyfishObservationHeatmap.as_view(),
        name='data_route_observation_heatmap',
        ),
    url(r'^route/list/?$',
        views.ObservationRouteList.as_view(),
        name='data_route_list',
        ),
    url(r'^species/list.json$',
        views.JSONJellyfishSpecieList.as_view(),
        name='data_species_json',
        ),
)
