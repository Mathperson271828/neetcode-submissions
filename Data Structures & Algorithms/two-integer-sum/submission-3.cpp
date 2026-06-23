class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indices;
        
        unordered_set<int> need2;
        for (int i = nums.size()-1; i >= 0; i--) {
            if (need2.find(nums[i]) != need2.end()) {
                indices.push_back(i);
            }
            else {
                need2.insert(target-nums[i]);
            }
        }
        unordered_set<int> need;
        for (int i = 0; i < nums.size(); i++) {
            if (need.find(nums[i]) != need.end()) {
                indices.push_back(i);
            }
            else {
                need.insert(target-nums[i]);
            }
        }

        return indices;
    }
};
