class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mapping;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];

            if (mapping.find(diff) != mapping.end()) {
                return {mapping[diff], i};
            }
            mapping.insert({nums[i], i});
        }
        return {};
    }
};
