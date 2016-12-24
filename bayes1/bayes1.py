import numpy

observations = [['Red', 'Sports', 'Imported'], ['Red', 'SUV', 'Domestic'],
                ['Black', 'Sports', 'Imported'], ['Blue', 'Sports', 'Domestic'],
                ['Blue', 'Sports', 'Domestic'], ['Red', 'SUV', 'Imported']]
classes = ['Y', 'N', 'Y', 'Y', 'N', 'Y']
tyeps_of_classes = ['N', 'Y']
types_of_observations = [['Red', 'Black', 'Blue'], ['Sports', 'SUV'], ['Imported', 'Domestic']]

#How to use this because it keeps on getting complicated and variables don't have any particular meaning
#Okay, so far, to find the probability of a class given an observation, pass the classes, and observations
#as it is and pass the index_of_type_of_observations as for the particular observation you want to find
#and
def find_conditional_probability(classes, observations, index_of_types_of_observations, index_of_index_of_type_of_observation,
                                  types_of_classes, types_of_observations):
    sum_of_conditional_probabilities=0
    highest_conditional_probability = 0
    highest_conditional_probability_index = 1000
    for i in range(len(types_of_classes)):
        class_in_classes = 0
        # observation_in_observations=0
        probability_of_class_given_observations = 0
        conditional_probability=0
        for j in range(len(classes)):
            if types_of_classes[i] is classes[j]:
                class_in_classes = class_in_classes + 1
        # for k in observations:
        #     if observations[k][index_of_types_of_observations] is types_of_observations[index_of_types_of_observations][k]:
        #         observation_in_observations=observation_in_observations+1
        for j in range(len(classes)):
            # for k in observations:
            if types_of_classes[i] is classes[j]:
                if observations[j][index_of_types_of_observations] is types_of_observations[index_of_types_of_observations][index_of_index_of_type_of_observation]:
                    probability_of_class_given_observations=probability_of_class_given_observations+1

        conditional_probability = probability_of_class_given_observations*class_in_classes

        sum_of_conditional_probabilities=sum_of_conditional_probabilities+conditional_probability

        if highest_conditional_probability<conditional_probability:
            highest_conditional_probability=conditional_probability
            highest_conditional_probability_index=i

    return (highest_conditional_probability/sum_of_conditional_probabilities)*100, tyeps_of_classes[highest_conditional_probability_index]


print(find_conditional_probability(classes, observations, 0, 2, tyeps_of_classes, types_of_observations))